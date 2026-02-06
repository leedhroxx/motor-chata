import pandas as pd

# 1) 원본 CSV 읽기
df = pd.read_csv("recall.csv", encoding="utf-8")

# car_name_full 결측은 빈 문자열로
df["car_name_full"] = df["car_name_full"].fillna("")

# 2) car_name_full을 ',' 기준으로 나누고 explode로 행 늘리기
#    → 새 컬럼 이름은 model
df_expanded = df.assign(
    model = df["car_name_full"].str.split(",")
).explode("model")

# 앞뒤 공백 제거
df_expanded["model"] = df_expanded["model"].astype(str).str.strip()

# model 이 비어있으면 버리기
df_expanded = df_expanded[df_expanded["model"] != ""]

# 3) 생산기간을 start_date / end_date 로 나누기
# 예: '2018-12-04 ~ 2020-10-24'
prod = df_expanded["생산기간"].fillna("")

# '~' 기준으로 앞/뒤 나누기
period_split = prod.str.split("~", n=1, expand=True)

df_expanded["start_date_str"] = period_split[0].str.strip()
df_expanded["end_date_str"]   = period_split[1].fillna("").str.strip()

# 문자열 → 날짜 (형식 안 맞으면 NaT)
df_expanded["start_date"] = pd.to_datetime(
    df_expanded["start_date_str"],
    format="%Y-%m-%d",
    errors="coerce"
)
df_expanded["end_date"] = pd.to_datetime(
    df_expanded["end_date_str"].replace("", pd.NA),
    format="%Y-%m-%d",
    errors="coerce"
)

# 4) 대상수량 숫자 컬럼 (선택)
if "대상수량" in df_expanded.columns:
    df_expanded["target_qty"] = (
        df_expanded["대상수량"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df_expanded["target_qty"] = pd.to_numeric(
        df_expanded["target_qty"],
        errors="coerce"
    )

# 5) 필요 없는 중간 컬럼 정리
df_expanded = df_expanded.drop(
    columns=["start_date_str", "end_date_str"],
    errors="ignore"  # 혹시 없으면 에러 안 나게
)

# 6) 새 CSV로 저장
df_expanded.to_csv("recall_info_expanded.csv",
                   index=False,
                   encoding="utf-8-sig")

print("완료. 행 개수:", len(df), "→", len(df_expanded))

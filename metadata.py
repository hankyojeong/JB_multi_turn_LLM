# 1_국내체류외국인.xlsx
payload1 = {
    "file_name": "1_국내체류외국인.xlsx",
    "table_name": "1_tb_resident_foreigners",
    "description": "국내 체류하고 있는 외국인을 단기체류, 등록외국인, 외국국적동포_거소신고의 3개 카테고리로 구분하고, 각 카테고리별 외국인 수를 월별로 집계한 데이터",
    "meta_description": """
schema:
  category: str   # {'단기체류','장기체류거소','장기체류등록'}
  cnt: int        # 인원수
  p_year: int     # 예: 2022, 2023, 2024, 2025
  p_month: int    # 1~12
}

notes:
  - 숫자/특수문자로 시작하는 식별자는 SQLite에서 "..."로 인용
  - dtype 강제: cnt,p_year,p_month는 숫자형으로 캐스팅 후 사용
""",
    "user_question": "2025년 4월 기준 국내 단기 체류 외국인 수는?"
}

# 2_장기체류외국인_지역별_현황.csv
payload2 = {
    "file_name": "2_장기체류외국인_지역별_현황.csv",
    "table_name": "2_tb_long_term_foreigners_by_region",
    "description": "장기체류 외국인 중 등록외국인과 외국국적동포의 거소현황을 집계한 데이터. table_nm 컬럼을 기준으로 국적(1), 체류자격(2), 행정동(3), 연령대(4)로 구분되어 있음.",
    "meta_description": """
- table_nm: 원본 테이블명 (문자형) (데이터 구분용: 1.국적, 2.체류자격, 3.행정동, 4.연령대)
- sido: 시도 (문자형)
- sigungu: 시군구 (문자형)
- adong: 행정동 (문자형)
- gender: 성별 (문자형)
- age: 나이 (문자형)
- cert: 체류자격 (문자형)
- nat_nm: 국적 (문자형)
- cnt: 외국인 수 (정수형)
- base_ym: 기준년월 (문자형)
- gbn: 장기체류구분 (문자형)
"""
}


# 3_외국인근로자.xlsx
payload3 = {
    "file_name": "3_외국인근로자.xlsx",
    "table_name": "3_tb_foreign_workers_permit",
    "description": "비전문취업(E-9) 비자를 가진 외국인 근로자의 업종/지역별 분포를 분기별로 집계한 데이터",
    "meta_description": """
- base_ym: 기준년월 (문자형)
- sido: 시도 (문자형)
- upjong: 업종 (문자형)
- cnt: 외국인 수 (정수형)
"""
}

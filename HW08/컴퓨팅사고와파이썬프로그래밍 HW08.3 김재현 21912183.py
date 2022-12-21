"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW08.3 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 입력받은 엑셀 파일을 Pandas DataFrame을 통해 분석하고 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.30
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.10.30	    v1.0	최초 작성
* JH KIM            2022.11.01      v1.1    리스트 수정
"""

import pandas as pd

def main():
    df = pd.read_excel('student_scores.xlsx')               # get data from excel file
    print("df =")
    print(df)

    df_col_avg = df.loc[:, ['Eng', 'Kor', 'Math', 'Sci']]   # Datafram에서 성적 부분만 추출
    print("\navgs_per_class =")
    print(df_col_avg.mean())                                # 과목별 평균 출력

    avgs_per_student = df_col_avg.mean(1)                   # 개인의 평균 추출
    df.loc[:, 'Avg'] = avgs_per_student                     # Datafram에 Avg열 추가

    print("\ndf_sorted_with_avg =")
    sorted_df = df.sort_values(by='Avg', ascending=False, inplace=True)     # sorting

    df_col_avg = df.loc[:, ['Eng', 'Kor', 'Math', 'Sci', 'Avg']]            # Avg를 포함한 평균
    df.loc[len(df)] = df_col_avg.mean(0)
    df.at[len(df) - 1, 'st_name'] = 'Total_Avg'
    print(df)                                                               # printout processed data
    with pd.ExcelWriter("processed_scores.xlsx") as excel_writer:           # Excel Writer
        print('Writing df to excel file')
        df.to_excel(excel_writer, sheet_name='Students Records')            # printout at Excel


if __name__ == "__main__":
    main()
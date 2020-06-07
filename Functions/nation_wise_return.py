import Functions.all_function as fn
import Functions.all_library as lib

def nation_wide_return():
    average_branch_return_df = lib.pd.read_sql_query("""select AUDTORG as Branch_name,ISNULL(sum(case when TRANSTYPE<>1 
                    then INVNETH *-1 end), 0) /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnAmount from OESalesSummery
                    where
                    left(TRANSDATE,6)=convert(varchar(6),getdate(),112)
                    group by AUDTORG
    				order by ReturnAmount DESC""", fn.conn)

    average_branch_return_information = average_branch_return_df['ReturnAmount'].tolist()
    Total_amount_of_return = sum(average_branch_return_information)
    Total_no_of_branches = len(average_branch_return_information)
    average_branch_return_amount = Total_amount_of_return / Total_no_of_branches
    lib.plt.subplots(figsize=(2, 3))
    lib.plt.text(0.5, 0.6, str('Return % -MTD \n'), horizontalalignment='center', fontsize=18,
    verticalalignment='center')
    lib.plt.text(0.5, 0.45, str(round(average_branch_return_amount, 2)) + str('%'), fontsize=18,
                 horizontalalignment='center',
                 verticalalignment='center', color='#ed4e19')
    lib.plt.axis('off')
    # lib.plt.show()
    lib.plt.savefig('./Images/13.Nation_wide_return.png')
    print('13. Nation Wide Return')

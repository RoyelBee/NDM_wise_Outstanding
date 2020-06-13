import Functions.all_function as fn
import Functions.all_library as lib
dirpath = lib.os.path.dirname(lib.os.path.realpath(__file__))


def top10_branch_return():
        top_ten_branch_return_df = lib.pd.read_sql_query("""
                            select left(AUDTORG,3) as Branch_name,
                            ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) 
                            /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnPercent 
                            from OESalesSummery
                            where
                            left(TRANSDATE,6)<convert(varchar(6),getdate(),112) 
                            group by AUDTORG
                            order by ReturnPercent desc

                                    """, fn.conn)

        top_ten_branch_return_df.to_csv(r'./Data/All_Branch_Return.csv', index=False, header=True)

        top_ten_branch_return_df = top_ten_branch_return_df.head(10)

        average_branch_return_df = lib.pd.read_sql_query("""select AUDTORG as Branch_name,ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) 
                        /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnPercent from OESalesSummery
                        where
                        left(TRANSDATE,6)<convert(varchar(6),getdate(),112)
                        group by AUDTORG
                        order by ReturnPercent DESC """, fn.conn)

        average_branch_return_information = average_branch_return_df['ReturnPercent'].tolist()
        Total_amount_of_return = sum(average_branch_return_information)
        Total_no_of_branches = len(average_branch_return_information)
        average_branch_return_amount = Total_amount_of_return / Total_no_of_branches
        average_branch_amount_list = []

        for i in range(0, 10):
            average_branch_amount_list.append(average_branch_return_amount)

        Branch_name = top_ten_branch_return_df['Branch_name'].values.tolist()
        y_pos = lib.np.arange(len(Branch_name))
        ReturnAmount = abs(top_ten_branch_return_df['ReturnPercent'])
        ReturnAmount = ReturnAmount.values.tolist()
        max_amount = max(ReturnAmount)
        color = '#418af2'
        fig, ax = lib.plt.subplots(figsize=(12.81, 4.8))
        rects1 = lib.plt.bar(y_pos, ReturnAmount, align='center', alpha=0.9, color=color)
        lib.plt.plot(y_pos, average_branch_amount_list, color='orange',linewidth=3)

        def autolabel(bars):
            loop = 0
            for bar in bars:
                show = ReturnAmount[loop]
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, height,
                        '%.2f' % (show) + '%', ha='center', va='bottom', fontsize=12, rotation=0, fontweight='bold')
                loop = loop + 1

        autolabel(rects1)
        lib.plt.xticks(y_pos, Branch_name, rotation='horizontal', fontsize='12')
        # lib.plt.yticks(lib.np.arange(0, round(max_amount) + (.6 * round(max_amount)), max_amount / 6), fontsize='12')
        lib.plt.yticks(lib.np.arange(0, 1.1, .1), fontsize=12)
        lib.plt.title("15. Top 10 Branch Return % - MTD", fontsize=16, fontweight='bold', color='#3e0a75')
        lib.plt.legend(['National Return %', 'Branch Return %'], loc='upper center', bbox_to_anchor=(0.5, -0.085),
                       fancybox=True, shadow=True, ncol=4)
        lib.plt.tight_layout()
        # lib.plt.show()
        lib.plt.savefig('./Images/15.top5_branch_return.png')
        print('15. Top 5 Branch Return')


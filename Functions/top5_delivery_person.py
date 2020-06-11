import Functions.all_function as fn
import Functions.all_library as lib

def top5_delivery_persons_return():
    try:
        delivery_man_wise_return_df = lib.pd.read_sql_query("""
        select top 5 TWO.ShortName as DPNAME,left(Two.AUDTORG,
        3) as BranchName, Sales.ReturnAmount from
                    (select  DPID, AUDTORG,ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnAmount from OESalesSummery
                    where
                    left(TRANSDATE,6)=convert(varchar(6),getdate(),112)
                    group by DPID,AUDTORG) as Sales
                    left join
                    (select   distinct AUDTORG,ShortName,DPID from DP_ShortName) as TWO
                    on Sales.DPID = TWO.DPID
                    and Sales.AUDTORG=TWO.AUDTORG
                    where TWO.ShortName is not null
                    and Sales.ReturnAmount>0
                    order by ReturnAmount DESC  """, fn.conn)

        average_delivery_man_wise_return_df = lib.pd.read_sql_query("""
                 select top 5 Sales.ReturnAmount from
                (select DPID, AUDTORG,ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnAmount from OESalesSummery
                where
                left(TRANSDATE,6)=convert(varchar(6),getdate(),112)
                group by DPID,AUDTORG) as Sales
                left join
                (select   distinct AUDTORG,ShortName,DPID from DP_ShortName) as TWO
                on Sales.DPID = TWO.DPID
                and Sales.AUDTORG=TWO.AUDTORG
                where TWO.ShortName is not null
                and Sales.ReturnAmount>0
                order by ReturnAmount DESC
                 """, fn.conn)

        average_delivery_information = average_delivery_man_wise_return_df['ReturnAmount'].tolist()
        Total_amount_of_return = sum(average_delivery_information)
        Total_no_of_delivery_person = len(average_delivery_information)
        average_delivery_amount = Total_amount_of_return / Total_no_of_delivery_person
        average_amount_list = []

        for i in range(0, 5):
            average_amount_list.append(average_delivery_amount)

        DPNAME = delivery_man_wise_return_df['DPNAME']
        y_pos = lib.np.arange(len(DPNAME))
        ReturnAmount = abs(delivery_man_wise_return_df['ReturnAmount'])
        ReturnAmount = ReturnAmount.values.tolist()
        Branch_name = delivery_man_wise_return_df['BranchName'].values.tolist()

        branch_final_name = []
        for val in Branch_name:
            branch_final_name.append(val + " - ")

        max_amount = max(ReturnAmount)
        color = '#418af2'
        fig, ax = lib.plt.subplots(figsize=(12.81, 4.8))
        rects1 = lib.plt.bar(y_pos, ReturnAmount, align='center', alpha=0.9, color=color)
        lib.plt.plot(y_pos, average_amount_list, color='orange')

        def autolabel(bars):
            loop = 0
            for bar in bars:
                show = ReturnAmount[loop]
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, (1.05 * height),
                        '%.2f' % (show) + '%', ha='center', va='bottom', fontsize=12, rotation=0, fontweight='bold')
                loop = loop + 1

        autolabel(rects1)
        lib.plt.xticks(y_pos, branch_final_name + DPNAME, rotation='horizontal', fontsize='12')
        lib.plt.yticks(lib.np.arange(0, round(max_amount) + (.6 * round(max_amount)), max_amount / 6), fontsize='12')
        lib.plt.title("16. Top 5 DP Return % - MTD", fontsize=16, fontweight='bold', color='#3e0a75')
        lib.plt.legend(['National Return %', 'DP Return %'], loc='upper center', bbox_to_anchor=(0.5, -0.085),
                       fancybox=True, shadow=True, ncol=4)
        lib.plt.tight_layout()
        # lib.plt.show()
        lib.plt.savefig('./Images/16.top5_delivery_persons_return.png')
        print('16. Top 5 Delivery persons return')
    except:
        print('Sorry! no. 16 chart Top 5 Delivery persons return could not be generated')
        lib.plt.subplots(figsize=(12.81, 4.8))
        lib.plt.text(.3, 1,"16. Top 5 DP Return % - MTD", fontsize=16, fontweight='bold', color='#3e0a75')
        lib.plt.text(.01, .5, 'Sorry! Due to data unavailability, the graph could not be generated.',fontsize=18,color='red')
        lib.plt.axis('off')
        lib.plt.savefig('./Images/16.top5_delivery_persons_return.png')
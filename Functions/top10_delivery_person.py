import Functions.all_function as fn
import Functions.all_library as lib


def top10_delivery_persons_return():
    try:
        delivery_man_wise_return_df = lib.pd.read_sql_query("""
                    select left(Sales.AUDTORG,3) + '-' +TWO.ShortName as DPNAME ,Sales.ReturnAmount as 
                    ReturnAmount from
                    (select  DPID, AUDTORG,
                    ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnAmount
                    from OESalesSummery
                    where
                    left(TRANSDATE,6)<convert(varchar(6),getdate(),112)
                    group by DPID,AUDTORG) as Sales
                    left join
                    (select   distinct AUDTORG,ShortName,DPID from DP_ShortName) as TWO
                    on Sales.DPID = TWO.DPID
                    and Sales.AUDTORG=TWO.AUDTORG
                    where TWO.ShortName is not null
                    and Sales.ReturnAmount>0
                    order by ReturnAmount DESC """, fn.conn)

        #delivery_man_wise_return_df.to_csv(r'./Data/All_Delivery_Persons_Return.csv', index=False, header=True)
        delivery_man_wise_return_df = delivery_man_wise_return_df.head(10)

        average_delivery_man_wise_return_df = lib.pd.read_sql_query("""
                 select Sales.ReturnAmount from
                (select  DPID, AUDTORG,
                ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnAmount
                from OESalesSummery
                where
                left(TRANSDATE,6)<convert(varchar(6),getdate(),112)
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
        # print(average_delivery_amount)
        average_amount_list = []
        for i in range(0, 10):
            average_amount_list.append(average_delivery_amount)
        DPNAME = delivery_man_wise_return_df['DPNAME']
        y_pos = lib.np.arange(len(DPNAME))
        ReturnAmount = abs(delivery_man_wise_return_df['ReturnAmount'])
        ReturnAmount = ReturnAmount.values.tolist()
        max_amount = max(ReturnAmount)
        color = '#418af2'
        fig, ax = lib.plt.subplots(figsize=(12.81, 4.8))
        rects1 = lib.plt.bar(y_pos, ReturnAmount, align='center', alpha=0.9, color=color)

        # lib.plt.plot(y_pos, average_amount_list, color='orange')
        def autolabel(bars):
            loop = 0
            for bar in bars:
                show = ReturnAmount[loop]
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, height,
                        '%.2f' % (show) + '%', ha='center', va='bottom', fontsize=12, rotation=0, fontweight='bold')
                loop = loop + 1

        autolabel(rects1)
        lib.plt.xticks(y_pos, DPNAME, rotation='horizontal', fontsize='12')
        lib.plt.yticks(lib.np.arange(0, 101, 10), fontsize='12')
        lib.plt.title("16. Top 10 DP Return % - MTD", fontsize=16, fontweight='bold', color='#3e0a75')
        lib.plt.legend(['DP Return %'], loc='best')
        lib.plt.tight_layout()
        # lib.plt.show()
        lib.plt.savefig('./Images/16.top5_delivery_persons_return.png')
        print('16. Top 5 Delivery persons return')
    except:
        print('Sorry! no. 16 chart Top 5 Delivery persons return could not be generated')
        lib.plt.subplots(figsize=(12.80, 4.8))
        lib.plt.text(.3, 1, "16. Top 5 DP Return % - MTD", fontsize=16, fontweight='bold', color='#3e0a75')
        lib.plt.text(.01, .5, 'Sorry! Due to data unavailability, the graph could not be generated.', fontsize=18,
                     color='red')
        lib.plt.axis('off')
        lib.plt.savefig('./Images/16.top5_delivery_persons_return.png')

import Functions.all_function as fn
import Functions.all_library as lib

def national_vs_ndm_return():
    try:
        ndm_anwar_df = lib.pd.read_sql_query("""
                    select ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) /ISNULL(sum(
                    case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnPercent from OESalesSummery
                    where
                    left(TRANSDATE,6)<convert(varchar(6),getdate(),112) 
                    and AUDTORG IN ('BOGSKF','MYMSKF', 'FRDSKF', 'TGLSKF', 'RAJSKF', 'SAVSKF')
                    order by ReturnPercent DESC 
                             """, fn.conn)
        anwar_return = ndm_anwar_df['ReturnPercent'].tolist()

        ndm_kamrul_df = lib.pd.read_sql_query("""
                select ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0)
                /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnPercent from OESalesSummery
                where
                left(TRANSDATE,6)<convert(varchar(6),getdate(),112) 
                and AUDTORG IN ('BSLSKF','COMSKF','JESSKF','KHLSKF','MIRSKF','PATSKF')
                order by ReturnPercent DESC
                        """, fn.conn)
        kamrul_return = ndm_kamrul_df['ReturnPercent'].tolist()

        ndm_atik_df = lib.pd.read_sql_query("""
                select ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 
                0) /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnPercent from OESalesSummery
                where
                left(TRANSDATE,6)<convert(varchar(6),getdate(),112) 
                and AUDTORG IN ('DNJSKF','GZPSKF','HZJSKF','KRNSKF','KSGSKF','MOTSKF','RNGSKF')
                order by ReturnPercent DESC
                         
                         """, fn.conn)
        atik_return = ndm_atik_df['ReturnPercent'].tolist()

        ndm_nurul_df = lib.pd.read_sql_query("""
                    select ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) 
                    /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnPercent from OESalesSummery
                    where
                    left(TRANSDATE,6)<convert(varchar(6),getdate(),112)
                    and AUDTORG IN ('FENSKF','MHKSKF','MLVSKF','NOKSKF','SYLSKF','VRBSKF')
                    order by ReturnPercent DESC
                            
                            """, fn.conn)
        nurul_return = ndm_nurul_df['ReturnPercent'].tolist()

        ndm_hafizur_df = lib.pd.read_sql_query("""
                        select ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) 
                        /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnPercent from OESalesSummery
                        where
                        left(TRANSDATE,6)<convert(varchar(6),getdate(),112)
                        and AUDTORG IN ('COXSKF','CTGSKF','CTNSKF','KUSSKF','NAJSKF','PBNSKF')
                        order by ReturnPercent DESC
                                
                                """, fn.conn)
        hafizur_return = ndm_hafizur_df['ReturnPercent'].tolist()

        average_branch_return_df = lib.pd.read_sql_query("""
                        select AUDTORG as Branch_name,ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) 
                        /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as AVGReturnPercent from 
                        OESalesSummery
                        where
                        left(TRANSDATE,6)<convert(varchar(6),getdate(),112)
                        group by AUDTORG
                        order by AVGReturnPercent DESC """, fn.conn)
        average_branch_return_information = average_branch_return_df['AVGReturnPercent'].tolist()
        Total_amount_of_return = sum(average_branch_return_information)
        Total_no_of_branches = len(average_branch_return_information)
        average_branch_return_amount = Total_amount_of_return / Total_no_of_branches
        array_of_ndm_return = [anwar_return[0], kamrul_return[0], atik_return[0], nurul_return[0], hafizur_return[0]]
        average_branch_amount_list = []
        for i in range(0, 5):
            average_branch_amount_list.append(average_branch_return_amount)

        name_of_ndms = ['Mr. Anwar', 'Mr. Kamrul', 'Mr. Atik', 'Mr. Nurul', 'Mr. Hafizur']
        y_pos = lib.np.arange(len(array_of_ndm_return))
        max_amount = max(array_of_ndm_return)
        color = '#418af2'
        fig, ax = lib.plt.subplots(figsize=(10.81, 3))
        rects1 = lib.plt.bar(y_pos, array_of_ndm_return, align='center', alpha=0.9, color=color)
        lib.plt.plot(y_pos, average_branch_amount_list, color='orange',linewidth=3)

        def autolabel(bars):
            loop = 0
            for bar in bars:
                show = array_of_ndm_return[loop]
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, (.99 * height),
                        '%.2f' % (show) + '%', ha='center', va='bottom', fontsize=12, rotation=0, fontweight='bold')
                loop = loop + 1

        autolabel(rects1)
        lib.plt.xticks(y_pos, name_of_ndms, rotation='horizontal', fontsize='12')
        # lib.plt.yticks(lib.np.arange(0, round(max_amount) + (.6 * round(max_amount)), max_amount / 6), fontsize='12')
        lib.plt.yticks(lib.np.arange(0, 1.1, .1), fontsize=12)
        lib.plt.title("14. NDM Wise Return % - MTD", fontsize=16, fontweight='bold', color='#3e0a75')
        lib.plt.legend(['National Return %', 'NDM Return %'], loc='upper center', bbox_to_anchor=(0.5, -0.085),
                   fancybox=True, shadow=True, ncol=4)
        lib.plt.tight_layout()
        print('14. Nation VS NDM Return')
        lib.plt.savefig('./Images/14.nation_vs_ndm_return.png')
    except:
        print('Sorry! no. 14 Nation VS NDM Return could not be generated')
        lib.plt.subplots(figsize=(10.81, 3))
        lib.plt.text(.3, 1, "14. NDM Wise Return % - MTD", fontsize=16, fontweight='bold', color='#3e0a75')
        lib.plt.text(.01, .5, 'Sorry! Due to data unavailability, the graph could not be generated.', fontsize=18,
                     color='red')
        lib.plt.axis('off')
        lib.plt.savefig('./Images/14.nation_vs_ndm_return.png')

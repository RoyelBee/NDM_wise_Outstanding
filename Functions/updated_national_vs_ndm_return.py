import Functions.all_function as fn
import Functions.all_library as lib

def national_vs_ndm_return():
    try:
        ndm_all_df = lib.pd.read_sql_query("""
                                        select 
                    NDM.SHORTNAME as 'NDM Name',
                    ISNULL(sum(case when TRANSTYPE<>1 then EXTINVMISC  *-1 end), 0) 
                    /ISNULL(sum(case when TRANSTYPE=1 then EXTINVMISC  end), 0)*100 as ReturnPercent 
                    from OESalesDetails
                    
                    left join NDM
                    on OESalesDetails.AUDTORG= NDM.BRANCH
                    where
                    left(TRANSDATE,6)=convert(varchar(6),getdate(),112)
                    group by SHORTNAME
                    order by ReturnPercent DESC
""", fn.conn)
        all_person_return = ndm_all_df['ReturnPercent'].tolist()

        average_branch_return_df = lib.pd.read_sql_query("""
                        select 
                        ISNULL(sum(case when TRANSTYPE<>1 then EXTINVMISC  *-1 end), 0) 
                        /ISNULL(sum(case when TRANSTYPE=1 then EXTINVMISC  end), 0)*100 as ReturnPercent 
                        from OESalesDetails
                        where left(TRANSDATE,6)=convert(varchar(6),getdate(),112) """, fn.conn)
        average_branch_return_information = average_branch_return_df['ReturnPercent'].tolist()
        average_branch_return_amount = average_branch_return_information[0]
        #print(average_branch_return_information[0])
        array_of_ndm_return = all_person_return
        average_branch_amount_list = []
        for i in range(0, 5):
            average_branch_amount_list.append(average_branch_return_amount)

        name_of_ndms = ndm_all_df['NDM Name'].tolist()
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
        # props = dict(boxstyle='round', pad=.3, facecolor='yellow', alpha=0.5, edgecolor='red')
        # lib.plt.text(3.88, 4.1, 'National return \n' + '       ' + str(round(average_branch_return_amount, 2)) + '%',
        #              fontsize=12, verticalalignment='center', bbox=props)
        lib.plt.xticks(y_pos, name_of_ndms, rotation='horizontal', fontsize='12')
        # lib.plt.yticks(lib.np.arange(0, round(max_amount) + (.6 * round(max_amount)), max_amount / 6), fontsize='12')
        lib.plt.yticks(lib.np.arange(0, 5.1, 1), fontsize=12)
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

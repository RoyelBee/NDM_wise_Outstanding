# #
# # # # --------- 1. Total Outstanding -------------------------------
# import Functions.outstanding as out
# out.totalOutstanding()
#
# # # ------- 2. Credit Outstanding -----------------------------------
# import Functions.credit_outstanding as credit
# credit.creditOutstanding()
#
# # #---. 3. NDM wise credit outstanding -------------------------------
# import Functions.updated_ndm_outstanding as ndm_out
# ndm_out.ndm_wise_outstanding()
#
# # # ---- 4. matured credit aging ----------------------------------
# import Functions.matured_credit_aging as ndm_matured
# ndm_matured.matured_credit()
# # #
# # # # # ----- 5. NDM matured credit aging ---------------------------
# import Functions.ndm_matured_credit_aging as ndm_aging
# ndm_aging.ndm_matured_credit_aging()
# #
# # # -------- 6. Branch wise matured  credit aging  -------------------
# import Functions.Second_updated_branch_wise_matured_credit as branch_matured
# branch_matured.branch_wise_matured_credit()
# #
# # # # -- 7. Total Non-matured credit aging ---------------------------
import Functions.updated_total_non_matured_credit_aging as non_matured_credit
non_matured_credit.total_non_matured_credit_aging()
#
# # # -- 8. NDM wise non-matured credit aging --------------------------
# import Functions.ndm_non_matured_credit_aging as ndm_non_matured
# ndm_non_matured.ndm_non_matured_credit_aging()
#
# # # --- 9. Branch wise non-matured credit aging --------------------
# import Functions.Second_updated_branch_wise_non_matured_credit as branch_non_matured
# branch_non_matured.branch_wise_non_matured_credit()
#
# # # ---10. Total Cash Drop Aging ----------------------------------
import Functions.updated_total_cashdrop_aging as cash_drop
# cash_drop.cashdrop_aging()
#
# # # ------------11. NDM wise cash drop aging ----------------------
# import Functions.NDM_wise_cash_drop_aging as ndm_cash_drop
# ndm_cash_drop.ndm_cash_drop()
#
# # # -- 12. Branch wise cash drop aging ----------------
# import Functions.Second_updated_branch_wise_cash_drop as branch_cash_drop2
# branch_cash_drop2.branch_wise_cash_drop_aging()
#
# # # ------ 13. Nation wide return ---------------------------------
# import Functions.updated_nation_wise_return as nation_return
# nation_return.nation_wide_return()
# # #
# # # # # -------14. Nation VS NDM Return ----------------------------
# import Functions.updated_national_vs_ndm_return as nation_vs_ndm
# nation_vs_ndm.national_vs_ndm_return()
# #
# # # -------15. Top 10 Branch Return -------------------------------
# import Functions.updated_top10_branch_return as top5_branch
# top5_branch.top10_branch_return()
#
# # # ----  16.Top 10 Delivery Persons Return Amount ----------------
# import Functions.updated_top10_delivery_person as delivery_persons_return
# delivery_persons_return.top10_delivery_persons_return()
#
# import Generate_all_csv as csvGenerator
# csvGenerator.All_csv_generator()
#
#
# # import Functions.kpi12 as test
# # test.branch_wise_cash_drop_aging()
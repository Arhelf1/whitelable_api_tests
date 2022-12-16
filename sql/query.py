# запросы
order_buy = "SELECT [WhiteLabelDev].[Trade].[Orders].[Order:ID]," \
            "[WhiteLabelDev].[Trade].[Orders].[LastName], " \
            "[WhiteLabelDev].[Trade].[Orders].[FirstName], " \
            "[WhiteLabelDev].[Trade].[Orders].[MiddleName], " \
            "[WhiteLabelDev].[Trade].[Orders].[Phone], " \
            "[WhiteLabelDev].[Trade].[Orders].[Price], " \
            "[WhiteLabelDev].[Trade].[Orders].[Qty]" \
            "FROM [WhiteLabelDev].[Trade].[Orders]" \
            "WHERE [WhiteLabelDev].[Trade].[Orders].[Order:ID] = ?"


order_create_sell = "SELECT [WhiteLabelDev].[Trade].[Orders].[Order:ID], " \
                    "[WhiteLabelDev].[Trade].[Orders].[LastName], " \
                    "[WhiteLabelDev].[Trade].[Orders].[FirstName]," \
                    "[WhiteLabelDev].[Trade].[Orders].[MiddleName]," \
                    "[WhiteLabelDev].[Trade].[Orders].[Phone]," \
                    "[WhiteLabelDev].[Trade].[Orders].[Price]," \
                    "[WhiteLabelDev].[Trade].[Orders].[Qty]," \
                    "[WhiteLabelDev].[Trade].[Orders].[Account]," \
                    "[WhiteLabelDev].[Trade].[Orders].[Bank]," \
                    "[WhiteLabelDev].[Trade].[Orders].[Bik]," \
                    "[WhiteLabelDev].[Trade].[Orders].[nnDoc]" \
                    "FROM [WhiteLabelDev].[Trade].[Orders]" \
                    "WHERE [WhiteLabelDev].[Trade].[Orders].[Order:ID] = ?"

check_sms = "SELECT Code FROM FinamEDO.Security.[Sended:SMS] " \
            "WHERE FinamEDO.Security.[Sended:SMS].[DocumentsID] = ?"

sms_by_user_id = "SELECT Code FROM FinamEDO.Security.[Sended:SMS] " \
            "WHERE FinamEDO.Security.[Sended:SMS].[Global:ID] = ?"

select_products_of_partner = """SELECT						[ProductId] as Id
                            ,Products.Description
                            FROM [WhitelabelTest_test_shared].[dbo].[PartnersProducts]
                            inner join Products
                            on PartnersProducts.ProductId = Products.Id
                            where PartnerId = 4 """
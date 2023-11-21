from database import destination_session, DestinationFreshPayFinance, session, FreshPayFinance, \
    DestinationWalletHistorique, WalletHistorique, BalanceHistorique, DestinationBalanceHistorique, \
    DrcFreshPayTransactionCommissions, DestinationDrcFreshPayTransactionCommissions


async def copy():
    # select last index from destination
    destination_index = destination_session.query(DestinationFreshPayFinance).order_by(
        DestinationFreshPayFinance.id.desc()).first()

    global source

    if destination_index is None:
        source = session.query(FreshPayFinance).all().limit(99999)
    else:
        source = session.query(FreshPayFinance).filter(FreshPayFinance.id > destination_index.id).limit(99999)

    if source is not None:
        for item in source:
            temp = DestinationFreshPayFinance(item.id, item.merchant_code, item.institution_name, item.method,
                                              item.currency,
                                              item.merchant_payout, item.merchant_deposit, item.comission_payout,
                                              item.comission_deposit, item.telco_payout, item.telco_deposit,
                                              item.freshpay_payout, item.freshpay_deposit, item.total_sent,
                                              item.total_received, item.created_at)

            destination_session.add(temp)
            destination_session.commit()

    print("FreshPay Finance - running finished")


async def copyWallet():
    # select last index from destination
    destination_index = destination_session.query(DestinationWalletHistorique).order_by(
        DestinationWalletHistorique.id.desc()).first()

    global source

    if destination_index is None:
        source = session.query(WalletHistorique).all().limit(99999)
    else:
        source = session.query(WalletHistorique).filter(WalletHistorique.id > destination_index.id).limit(99999)

    if source is not None:
        for item in source:
            temp = DestinationWalletHistorique(item.id, item.status, item.action, item.merchant_code, item.currency,
                                               item.amount, item.merchant_comission, item.created_at,
                                               item.paydrc_reference, item.method, item.wallet_code,
                                               item.amount_transac, item.wallet_current_amount)

            destination_session.add(temp)
            destination_session.commit()

    print("Wallet Historique - running finished")


async def copyBalance():
    # select last index from destination
    destination_index = destination_session.query(DestinationBalanceHistorique).order_by(
        DestinationBalanceHistorique.id.desc()).first()

    global source

    if destination_index is None:
        source = session.query(BalanceHistorique).all().limit(99999)
    else:
        source = session.query(BalanceHistorique).filter(BalanceHistorique.id > destination_index.id).limit(99999)

    if source is not None:
        for item in source:
            temp = DestinationBalanceHistorique(item.id, item.status, item.action, item.method, item.currency,
                                                item.balance_telco, item.balance_freshpay, item.telco_comission,
                                                item.freshpay_comission, item.created_at, item.paydrc_reference,
                                                item.amount_transac, item.balance_current_telco,
                                                item.balance_current_freshpay)

            destination_session.add(temp)
            destination_session.commit()

    print("Balance Historique - running finished")


async def copyTransactionCommission():
    # select last index from destination
    destination_index = destination_session.query(DestinationDrcFreshPayTransactionCommissions).order_by(
        DestinationDrcFreshPayTransactionCommissions.id.desc()).first()

    global source

    if destination_index is None:
        source = session.query(DrcFreshPayTransactionCommissions).all().limit(99999)
    else:
        source = session.query(DrcFreshPayTransactionCommissions).filter(
            DrcFreshPayTransactionCommissions.id > destination_index.id).limit(99999)

    if source is not None:
        for item in source:
            temp = DestinationDrcFreshPayTransactionCommissions(item.id, item.amount, item.method, item.merchant_code,
                                                                item.currency, item.status, item.paydrc_reference,
                                                                item.switch_reference, item.freshpay_comission,
                                                                item.telco_reference, item.amount_freshpay,
                                                                item.created_at, item.updated_at)

            destination_session.add(temp)
            destination_session.commit()

    print("Transaction Commission - running finished")

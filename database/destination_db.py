import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Integer, FLOAT, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
load_dotenv()


class DestinationFreshPayFinance(Base):
    __tablename__ = 'freshpay_finance'

    id = Column("id", Integer, primary_key=True)
    merchant_code = Column('merchant_code', String(255))
    institution_name = Column('institution_name', String(255))
    method = Column('method', String(255))
    currency = Column('currency', String(255))
    merchant_payout = Column('merchant_payout', FLOAT)
    merchant_deposit = Column('merchant_deposit', FLOAT)
    comission_payout = Column('comission_payout', FLOAT)
    comission_deposit = Column('comission_deposit', FLOAT)
    telco_payout = Column('telco_payout', FLOAT)
    telco_deposit = Column('telco_deposit', FLOAT)
    freshpay_payout = Column('freshpay_payout', FLOAT)
    freshpay_deposit = Column('freshpay_deposit', FLOAT)
    total_sent = Column('total_sent', FLOAT)
    total_received = Column('total_received', FLOAT)
    created_at = Column('created_at', DATETIME)

    def __init__(self, id: int,
                 merchant_code: str,
                 institution_name: str,
                 method: str,
                 currency: str,
                 merchant_payout: float,
                 merchant_deposit: float,
                 comission_payout: float,
                 comission_deposit: float,
                 telco_payout: float,
                 telco_deposit: float,
                 freshpay_payout: float,
                 freshpay_deposit: float,
                 total_sent: float,
                 total_received: float,
                 created_at: str,
                 ):
        self.id = id
        self.merchant_code = merchant_code
        self.institution_name = institution_name
        self.method = method
        self.currency = currency
        self.merchant_payout = merchant_payout
        self.merchant_deposit = merchant_deposit
        self.comission_payout = comission_payout
        self.comission_deposit = comission_deposit
        self.telco_payout = telco_payout
        self.telco_deposit = telco_deposit
        self.freshpay_payout = freshpay_payout
        self.freshpay_deposit = freshpay_deposit
        self.total_sent = total_sent
        self.total_received = total_received
        self.created_at = created_at


class DestinationWalletHistorique(Base):
    __tablename__ = 'wallet_historique'

    id = Column('id', Integer, primary_key=True)
    status = Column('status', String(255))
    action = Column('action', String(255))
    merchant_code = Column('merchant_code', String(255))
    currency = Column('currency', String(255))
    amount = Column('amount', FLOAT)
    merchant_comission = Column('merchant_comission', FLOAT)
    created_at = Column('created_at', DATETIME)
    paydrc_reference = Column('paydrc_reference', String(255))
    method = Column('method', String(30))
    wallet_code = Column('wallet_code', String(50))
    amount_transac = Column('amount_transac', FLOAT)
    wallet_current_amount = Column('wallet_current_amount', FLOAT)

    def __init__(self, id: int, status: str, action: str, merchant_code: str, currency: str, amount: float,
                 merchant_comission: float, created_at: str,
                 paydrc_reference: str, method: str, wallet_code: str, amount_transac: float,
                 wallet_current_amount: float):
        self.id = id
        self.status = status
        self.action = action
        self.merchant_code = merchant_code
        self.currency = currency
        self.amount = amount
        self.merchant_comission = merchant_comission
        self.created_at = created_at
        self.paydrc_reference = paydrc_reference
        self.method = method
        self.wallet_code = wallet_code
        self.amount_transac = amount_transac
        self.wallet_current_amount = wallet_current_amount


class DestinationBalanceHistorique(Base):
    __tablename__ = 'balance_historique'

    id = Column('id', Integer, primary_key=True)
    status = Column('status', String(30))
    action = Column('action', String(30))
    method = Column('method', String(50))
    currency = Column('currency', String(10))
    balance_telco = Column('balance_telco', FLOAT)
    balance_freshpay = Column('balance_freshpay', FLOAT)
    telco_comission = Column('telco_comission', FLOAT)
    freshpay_comission = Column('freshpay_comission', FLOAT)
    created_at = Column('created_at', DATETIME)
    paydrc_reference = Column('paydrc_reference', String(100))
    amount_transac = Column('amount_transac', FLOAT)
    balance_current_telco = Column('balance_current_telco', FLOAT)
    balance_current_freshpay = Column('balance_current_freshpay', FLOAT)

    def __init__(self, id: int,
                 status: str,
                 action: str,
                 method: str,
                 currency: str,
                 balance_telco: float,
                 balance_freshpay: float,
                 telco_comission: float,
                 freshpay_comission: float,
                 created_at: str,
                 paydrc_reference: str,
                 amount_transac: float,
                 balance_current_telco: float,
                 balance_current_freshpay: float
                 ):
        self.id = id
        self.status = status
        self.action = action
        self.method = method
        self.currency = currency
        self.balance_telco = balance_telco
        self.balance_freshpay = balance_freshpay
        self.telco_comission = telco_comission
        self.freshpay_comission = freshpay_comission
        self.created_at = created_at
        self.paydrc_reference = paydrc_reference
        self.amount_transac = amount_transac
        self.balance_current_telco = balance_current_telco
        self.balance_current_freshpay = balance_current_freshpay


class DestinationDrcFreshPayTransactionCommissions(Base):
    __tablename__ = 'drc_freshpay_transaction_comission'

    id = Column('id', Integer, primary_key=True)
    amount = Column('amount', String(100))
    method = Column('method', String(80))
    merchant_code = Column('merchant_code', String(80))
    currency = Column('currency', String(80))
    status = Column('status', String(80))
    paydrc_reference = Column('paydrc_reference', String(80))
    switch_reference = Column('switch_reference', String(80))
    freshpay_comission = Column('freshpay_comission', String(80))
    telco_reference = Column('telco_reference', String(80))
    amount_freshpay = Column('amount_freshpay', String(80))
    created_at = Column('created_at', DATETIME)
    updated_at = Column('updated_at', DATETIME)

    def __init__(self, id: str,
                 amount: str,
                 method: str,
                 merchant_code: str,
                 currency: str,
                 status: str,
                 paydrc_reference: str,
                 switch_reference: str,
                 freshpay_comission: str,
                 telco_reference: str,
                 amount_freshpay: str,
                 created_at: str,
                 updated_at: str
                 ):
        self.id = id
        self.amount = amount
        self.method = method
        self.merchant_code = merchant_code
        self.currency = currency
        self.status = status
        self.paydrc_reference = paydrc_reference
        self.switch_reference = switch_reference
        self.freshpay_comission = freshpay_comission
        self.telco_reference = telco_reference
        self.amount_freshpay = amount_freshpay
        self.created_at = created_at
        self.updated_at = updated_at


engine = create_engine(
    f"mysql+pymysql://{os.getenv('REPORTING_DB_USER')}:%s@{os.getenv('REPORTING_DB_IP')}/reporting" % quote_plus(
        f"{os.getenv('REPORTING_DB_PASS')}"),
    echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
destination_session = Session()

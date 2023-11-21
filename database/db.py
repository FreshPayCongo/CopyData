import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
load_dotenv()

engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:%s@{os.getenv('DB_IP')}/freshpay_online?ssl_ca={os.getenv('SSL_CA')}&ssl_cert={os.getenv('SSL_CLIENT')}&ssl_key={os.getenv('SSL_KEY')}&ssl_check_hostname=false" % quote_plus(
        f"{os.getenv('DB_PASS')}"),
    echo=True)

Base.metadata.create_all(bind=engine)


class FreshPayFinance(Base):
    __table__ = Table('freshpay_finance', Base.metadata, autoload_with=engine)


class BalanceHistorique(Base):
    __table__ = Table('balance_historique', Base.metadata, autoload_with=engine)


class WalletHistorique(Base):
    __table__ = Table('wallet_historique', Base.metadata, autoload_with=engine)


class DrcFreshPayTransactionCommissions(Base):
    __table__ = Table('drc_freshpay_transaction_comission', Base.metadata, autoload_with=engine)


Session = sessionmaker(bind=engine)
session = Session()

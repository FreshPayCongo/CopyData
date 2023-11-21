from fastapi import FastAPI
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_scheduler import SchedulerAdmin

from utils import copy, copyBalance, copyWallet, copyTransactionCommission

app = FastAPI()

site = AdminSite(settings=Settings(database_url_async="mysql+asyncmy://nathan:nathan@localhost/alchemy"))

scheduler = SchedulerAdmin.bind(site)


@scheduler.scheduled_job('interval', seconds=5400)
async def interval_task():
    await copy()
    await copyWallet()
    await copyTransactionCommission()
    await copyBalance()


site.mount_app(app)


@app.on_event('startup')
async def startup():
    scheduler.start()

import ydb

driver_config = ydb.DriverConfig(
    'grpcs://ydb.serverless.yandexcloud.net:2135', '/ru-central1/b1gphm1dcohckjslorj5/etnhai8sgdi0irmbbnbu',
    credentials=ydb.construct_credentials_from_environ(),
    root_certificates=ydb.load_ydb_root_certificate(),
)
print(driver_config)
with ydb.Driver(driver_config) as driver:
    try:
        driver.wait(timeout=15)
    except TimeoutError:
        print("Connect failed to YDB")
        print("Last reported errors by discovery:")
        print(driver.discovery_debug_details())

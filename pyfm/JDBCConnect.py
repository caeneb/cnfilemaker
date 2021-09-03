import jaydebeapi


class FileMaker:
    def __init__(self, driver, server, database, username, password):
        self.connect = jaydebeapi.connect(
            'com.filemaker.jdbc.Driver',
            f'jdbc:filemaker://{server}/{database}?user={username}&password={password}',
            ['', ''],
            driver
        )
        self.cursor = self.connect.cursor()

    def execute(self, sql, parameters: list = []):
        if parameters:
            self.cursor.execute(sql, parameters)
        else:
            self.cursor.execute(sql)

        results = self.cursor.fetchall()

        return results

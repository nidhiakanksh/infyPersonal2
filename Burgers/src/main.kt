import java.sql.Connection
import java.sql.DriverManager
import java.sql.Time
import java.sql.Timestamp
import java.util.*
import kotlin.time.TimeSource

private const val SCHEMA = "REGISTERED_PATIENTS_DB"
private const val TABLE = "PATIENT_INFO"

fun main(args: Array<String>) {
    val properties = Properties()

    //Populate the properties file with user name and password
    with(properties) {
        put("user", "root")
        put("password", "GaTech340/340")
    }

    //Open a connection to the database
    DriverManager
        .getConnection("jdbc:" + "mysql" + "://" +"127.0.0.1" +":" + "3306" + "/" +"",   properties)
        .use { connection ->
                 connection.setAutoCommit(false);
                 prepareTable(connection)
                 insertItems(connection)
        }

}

private fun prepareTable(connection: Connection) {
    val metaData = connection.metaData
    val rs = metaData.getTables(null, SCHEMA, TABLE, null)
    //(rs.next())                                                                                        //ask@sujit
    if (!rs.next()) {
        createTable(connection)
    } else {
        truncateTable(connection)
    }
}


private fun createTable(connection: Connection) {
    val sql = """
         CREATE TABLE $SCHEMA.$TABLE (
            ID int primary key,
            FIRST_NAME varchar(30),
            LAST_NAME varchar(30),
            YEAR_OF_BIRTH year,
            PHONE varchar(10), 
            REG_TIMESTAMP varchar(30),
            SEX varchar(1)
           );         
        """.trimMargin()
    with(connection) {
        createStatement().execute(sql)
        commit()
    }
}

private fun truncateTable(connection: Connection) {
    val sql = "TRUNCATE TABLE $SCHEMA.$TABLE"
    with (connection) {
        createStatement().execute(sql)
        commit()
    }
}

private fun insertRow(connection: Connection, id: Int, first_name: String, last_name: String,year_of_birth: Int, phone: String, reg_timestamp: String, sex: String) {
    val sql = "INSERT INTO $SCHEMA.$TABLE VALUES ($id, $first_name, $last_name, $year_of_birth, $phone, $reg_timestamp, $sex)"
    with(connection) {
        createStatement().execute(sql)
        commit()
    }
}

private fun insertItems(connection: Connection) {
    val regTimestamp="'"+Timestamp(System.currentTimeMillis()).toString()+"'"
    insertRow(connection, 1,"'LEWIS'","'HAMILTON'",1985,"'1234567890'",regTimestamp,"'M'")
    insertRow(connection, 2,"'MAX'","'VERSTAPPEN'",1997,"'1234567891'",regTimestamp,"'M'")
    insertRow(connection, 3,"'TATIANA'","'CLAEDRON'",1994,"'1234567892'",regTimestamp,"'F'")
    insertRow(connection, 4,"'LANCE'","'STROLL'",1999,"'1234567893'",regTimestamp,"'M'")
    insertRow(connection, 5,"'CLAIRE'","'WILLIAMS'",1972,"'1234567899'",regTimestamp,"'F'")

}

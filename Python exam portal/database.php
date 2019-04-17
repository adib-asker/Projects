 

<?php
# SK Adib Asker, CS 490,Part 1: Alpha
/*
$db_host = "sql.njit.edu";
$db_user = "sia23";
$db_password = "bIokHCwRD";
$db_name = "sia23";
$db = new PDO("mysql:host=$db_host;dbname=$db_name", $db_user,$db_password);
$conn=mysqli_connect($db_host ,$db_user,$db_password,$db_name);
*/


#/*
define ('DB_HOST','sql1.njit.edu');
define ('DB_USER','sia23');
define ('DB_PASS','bIokHCwRD');
define ('DB_NAME','sia23');

$dsn = "mysql:host=".DB_HOST.";dbname=".DB_NAME.";charset=utf8";
$db = new PDO($dsn, DB_USER, DB_PASS);
#*/

?>
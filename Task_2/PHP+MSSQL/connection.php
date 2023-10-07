<?php

$serverName = "MACHONGNAM\SQLEXPRESS, 1433";
$database = "task_2";
$uid = "sa";
$pass = "1234";

$connection = array(
    "Database" => $database,
    "UID" => $uid,
    "PWD" => $pass
);

$conn = sqlsrv_connect($serverName, $connection);
if(!$conn) {
    echo "<script type='text/javascript'>alert('Connection failed!');</script>";
    die(print_r(sqlsrv_errors(),true));
}

?>
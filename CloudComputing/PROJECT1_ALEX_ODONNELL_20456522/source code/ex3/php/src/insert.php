
<?php

//These are the defined authentication environment in the db service

// The MySQL service named in the docker-compose.yml.
$host = 'db';

// Database use name
$user = 'MYSQL_USER';

//database user password
$pass = 'MYSQL_PASSWORD';

// check the MySQL connection status
$conn = new mysqli($host, $user, $pass);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
   // echo "Connected to MySQL server successfully!";
}

$sql="INSERT INTO MYSQL_DATABASE.users (id, username,password)
VALUES ('$_POST[id]', '$_POST[fname]','$_POST[lname]')";

if (!$conn->query($sql)) {
    die("Error: " . $conn->error);

}
else{
    echo "1 record added";
}



echo "<br>";
echo "<br>";
echo "<br>";
echo "TABLE DATA: id name pass";
$sql = 'SELECT * FROM MYSQL_DATABASE.users';

if ($result = $conn->query($sql)) {
    while ($data = $result->fetch_object()) {
        echo "<br>";
        echo $data->id . " " . $data->username . " " . $data->password;
    }
}
echo "<br>";
echo "Go back to insert more data";

?>

</body>

</html>


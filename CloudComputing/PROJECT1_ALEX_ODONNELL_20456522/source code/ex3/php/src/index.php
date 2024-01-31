<html>
<body>
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
    echo "Connected to MySQL server successfully!";
}

echo "<br>";
echo "<br>";
echo "<br>";

$mydatabase = 'MYSQL_DATABASE';
$sql = 'Create table MYSQL_DATABASE.users (
    id int not null auto_increment,
    username text not null,
    password text not null,
    primary key (id)
)';

if ($conn->query($sql) === TRUE) {
    echo "Table users created successfully";
  } else {
   // echo "Error creating table: " . $conn->error;
  }

  echo "<br>";
  echo "<br>";
  echo "<br>";

?>

<form action="insert.php" method="post">
    ID: <input type="int" name="id" /><br><br>
    Firstname: <input type="text" name="fname" /><br><br>
    password: <input type="text" name="lname" /><br><br>
    <input type="submit" />
</form>
</body>
</html>

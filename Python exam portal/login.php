
<?php
#SK Adib Asker, CS 490, Part 1: Alpha


$database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");

 
//$name="sia23";$pass="123456";

#isset determine if a variable is set and is not NULL
if(isset($_POST['name'])) $name = $_POST['name'];
if(isset($_POST['pass'])) $pass = $_POST['pass'];


#Change password to Hash
$md5pass = md5($pass);

#This is a query
$query = mysqli_query($database, " SELECT * FROM Users where  UCID like '$name' and Password like '$md5pass' ");
$result = mysqli_fetch_assoc($query);

#This is for checking that database is actually working	
/*
if($result) 
  {
	echo "Login Is Successful ";
  }
else 
  {
	echo "Login Is Unsuccessful ";
  }	
*/

if(!$result) 
  {
  $data=array("UCID"=>"none","authority"=>"none","userid"=>"none");
  }
else 
  {
	  
     $data=array("UCID"=>$result['UCID'],
					"authority"=>$result['Authority'],
					"userid"=>$result['Id']);
  }	
  echo json_encode($data);

 
 
?>

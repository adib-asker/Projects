<?php
	
  $database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	 
	
	if(isset($_POST['examname'])) $examname = $_POST['examname'];


 
 $sql= mysqli_query($database," SELECT * FROM exam where  examname like '$examname'");
 while($result= mysqli_fetch_assoc($sql))
 {
  $data[]=array("id"=>$result['id'],"question"=>$result['question'],"testcase"=>$result['testcase'],"points"=>$result['points']);
  }
  echo json_encode($data);
?>
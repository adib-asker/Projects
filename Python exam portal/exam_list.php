<?php
	# Sk adib asker, cs490, part 2: beta
$database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
	if(isset($_POST['examname'])) $examname = $_POST['examname'];
	
	$sql= mysqli_query($database, "SELECT DISTINCT examname FROM exam");
	
  while($row= mysqli_fetch_assoc($sql))
  {
		$data[]=array('examname'=> $row['examname']);
	}
	echo json_encode($data);
?>

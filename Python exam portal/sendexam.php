<?php
	# Sk adib asker, cs490, part 2: beta
$database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
	if(isset($_POST['points'])) $points = $_POST['points'];
	if(isset($_POST['question'])) $question = $_POST['question'];
  if(isset($_POST['examname'])) $examname = $_POST['examname'];
	if(isset($_POST['testcase'])) $testcase = $_POST['testcase'];
	$sql= mysqli_query($database, "SELECT * FROM exam ");
	
  while($row= mysqli_fetch_assoc($sql))
  {
		$data[]=array('id'=>$row['id'],'examname'=> $row['examname'], 'question'=> $row['question'],'testcase'=>$row['testcase'], 'points'=>$row['points']);
	}
	echo json_encode($data);
?>

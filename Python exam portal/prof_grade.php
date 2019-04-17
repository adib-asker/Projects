<?php
	# Sk adib asker, cs490, part 2: beta
$database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
	if(isset($_POST['grade'])) $grade = $_POST['grade'];

	$sql= mysqli_query($database, "SELECT * FROM gradedexam ");
	
  while($row= mysqli_fetch_assoc($sql))
  {
		$data[]=array('id'=>$row['id'], 'ucid'=>$row['ucid'],'examname'=>$row['examname'] ,'grade'=> $row['grade'],'result'=>$row['result'],'testcase'=>$row['testcase'],'answer'=>$row['answer'],'topgrade'=>$row['topgrade'],'comments'=>$row['comments'],'released'=>$row['released']);
	}
	echo json_encode($data);
?>

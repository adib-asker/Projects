<?php
	# Sk adib asker, cs490, part 2: beta
$database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
	if(isset($_POST['ucid'])) $ucid = $_POST['ucid'];
	if(isset($_POST['grade'])) $grade = $_POST['grade'];
	if(isset($_POST['result'])) $result = $_POST['result'];
 if(isset($_POST['examname'])) $examname = $_POST['examname'];
	if(isset($_POST['topgrade'])) $topgrade = $_POST['topgrade'];
	if(isset($_POST['comments'])) $comments = $_POST['comments'];
 if(isset($_POST['released'])) $released = $_POST['released'];
 if(isset($_POST['testcase'])) $testcase = $_POST['testcase'];
	if(isset($_POST['answer'])) $answer = $_POST['answer'];
	$sql= mysqli_query($database, "SELECT * FROM gradedexam where ucid like '$ucid' ");
	
  while($row = mysqli_fetch_assoc($sql))
  {
		$data[]=array('id'=>$row['id'], 'ucid'=>$row['ucid'],'examname'=>$row['examname'] ,'result'=>$row['result'],'testcase'=> $row['testcase'],'answer'=> $row['answer'],'grade'=> $row['grade'],'topgrade'=>$row['topgrade'],'comments'=>$row['comments'],'released'=>$row['released']);
	}
	echo json_encode($data);
?>

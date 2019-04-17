
<?php
  # Sk adib asker, cs490, part 2: beta
  
  $database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
  if(isset($_POST['ucid'])) $ucid = $_POST['ucid'];
  if(isset($_POST['released'])) $released = $_POST['released'];
 
  
  
  
  $sql = mysqli_query($database, "SELECT * FROM gradedexam where ucid like '$ucid' and released like 'Y' ");
  while($result= mysqli_fetch_assoc($sql))
  {  
  

   $data[]=array("ucid"=>$result['ucid'],"examname"=>$result['examname'],"result"=>$result['result'],'testcase'=>$result['testcase'],'answer'=>$result['answer'], "grade"=>$result['grade'], "topgrade"=>$result['topgrade'],"comments"=>$result['comments']);
   
  }
   
  echo json_encode($data);
  
?>
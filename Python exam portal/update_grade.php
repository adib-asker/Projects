
<?php
  # Sk adib asker, cs490, part 2: beta
  
  $database = mysqli_connect("sql1.njit.edu","sia23","bIokHCwRD","sia23");
	
  if(isset($_POST['ucid'])) $ucid = $_POST['ucid'];
  if(isset($_POST['examname'])) $examname = $_POST['examname'];
  if(isset($_POST['released'])) $released = $_POST['released'];
  if(isset($_POST['comments'])) $comments = $_POST['comments'];
  
  
  
  $sql = mysqli_query($database, "UPDATE `gradedexam` set `released`='$released', `comments`='$comments' where `ucid`='$ucid' and `examname`='$examname' ");
  
  if (sql)
  {
   echo "Updated";
  }
  else
  {
  
   echo "Not updated";
  }
  if(isset($_POST['grade'])){
  
   $grade = $_POST['grade'];
   $sql = mysqli_query($database, "UPDATE `gradedexam` set `grade`='$grade' where `ucid`='$ucid' and `examname`='$examname' ");
   
   
   
  }
?>



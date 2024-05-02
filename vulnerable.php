<?php
$articleid = $_GET['article'];
$stmt = $pdo->prepare('SELECT * FROM articles WHERE articleid = :articleid');
$stmt->execute(['articleid' => $articleid]);
?>
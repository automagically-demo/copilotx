$articleid = $_GET['article'];
$db = new PDO('mysql:host=localhost;dbname=testdb;charset=utf8', 'username', 'password');

$query = $db->prepare("SELECT * FROM articles WHERE articleid = :articleid");
$query->execute(['articleid' => $articleid]);
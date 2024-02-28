$articleid = $_GET['article'];

$db = new PDO('mysql:host=localhost;dbname=testdb;charset=utf8', 'username', 'password');

$stmt = $db->prepare("SELECT * FROM articles WHERE articleid = :articleid");
$stmt->execute(array(':articleid' => $articleid));

$result = $stmt->fetchAll();
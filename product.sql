-- --------------------------------------------------------
-- 主機:                           127.0.0.1
-- 伺服器版本:                        10.8.3-MariaDB - mariadb.org binary distribution
-- 伺服器作業系統:                      Win64
-- HeidiSQL 版本:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- 傾印  資料表 market.myapp_productmodel 結構
CREATE TABLE IF NOT EXISTS `myapp_productmodel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `pname` varchar(30) NOT NULL,
  `pprice` int(11) NOT NULL,
  `pimage` varchar(40) NOT NULL,
  `pdescription` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- 正在傾印表格  market.myapp_productmodel 的資料：~8 rows (近似值)
/*!40000 ALTER TABLE `myapp_productmodel` DISABLE KEYS */;
INSERT INTO `myapp_productmodel` (`id`, `pname`, `pprice`, `pimage`, `pdescription`) VALUES
	(1, '萬花筒寫輪眼(左眼)', 100000000, 'eye1.png', '宇智波斑的萬花筒寫輪眼，擁有它可實現無現月讀的能力。'),
	(2, '萬花筒寫輪眼(右眼)', 100000000, 'eye2.png', '宇智波斑的萬花筒寫輪眼，擁有它可實現無現月讀的能力。'),
	(3, '木葉護額/佐助版', 2000, 'Forehead1.png', '宇智波佐助簽名過的的木葉護額，戴上它馬上潮度百分百。'),
	(4, '木葉護額/鳴人版', 2000, 'Forehead2.png', '漩渦鳴人加持的木葉護額，戴上它主角威能增力90%，還可免費前往妙木山參觀乙次。'),
	(5, '苦無+起爆符', 5000, 'Kunai_1.png', '春野櫻施放櫻吹雪大招時遺留下的未爆彈(?)，殘留了春野櫻身上的芬芳，宅男們千萬不可錯過。'),
	(6, '苦無+起爆符', 5000, 'Kunai_2.png', '春野櫻施放櫻吹雪大招時遺留下的未爆彈(?)，殘留了春野櫻身上的芬芳，宅男們千萬不可錯過。'),
	(7, '軍糧丸', 200, 'MilitaryRationsPill_1.png', '外出補給好妙方，增加戰鬥持久力。內含春野櫻獨家配方'),
	(8, '軍糧丸', 200, 'MilitaryRationsPill_2.png', '外出補給好妙方，增加戰鬥持久力。內含春野櫻獨家配方');
/*!40000 ALTER TABLE `myapp_productmodel` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

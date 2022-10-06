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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- 正在傾印表格  market.myapp_productmodel 的資料：~14 rows (近似值)
/*!40000 ALTER TABLE `myapp_productmodel` DISABLE KEYS */;
-- INSERT INTO `myapp_productmodel` (`id`, `pname`, `pprice`, `pimage`, `pdescription`) VALUES
-- 	(1, '萬花筒寫輪眼(左眼)', 100000000, 'eye1.png', '宇智波斑的萬花筒寫輪眼，您不用大義滅親就可獲得宇智波一族的強大力量，擁有它可實現無限月讀的能力!'),
-- 	(2, '萬花筒寫輪眼(右眼)', 100000000, 'eye2.png', '宇智波斑的萬花筒寫輪眼，您不用大義滅親就可獲得宇智波一族的強大力量，擁有它可實現無限月讀的能力!'),
-- 	(3, '木葉忍者護額', 2000, 'Forehead1.png', '木葉忍者村的強韌護具，每一具皆由25年以上資歷鑄造師精心鑄型，並由10名上忍注入查克拉打造而成!'),
-- 	(4, '木葉忍者護額', 2000, 'Forehead2.png', '木葉忍者村的強韌護具，每一具皆由25年以上資歷鑄造師精心鑄型，並由10名上忍注入查克拉打造而成!'),
-- 	(5, '苦無+起爆符', 5000, 'Kunai_1.png', '春野櫻施放櫻吹雪大招時遺留下的未爆彈(?)，殘留了春野櫻身上的芬芳，宅男們千萬不可錯過。'),
-- 	(6, '苦無+起爆符', 5000, 'Kunai_2.png', '春野櫻施放櫻吹雪大招時遺留下的未爆彈(?)，殘留了春野櫻身上的芬芳，宅男們千萬不可錯過。'),
-- 	(7, '軍糧丸', 200, 'MilitaryRationsPill_1.png', '外出補給好妙方，增加戰鬥持久力並恢復體力與查克拉。採火之國森林新鮮藥草配製，內含春野櫻獨家配方'),
-- 	(8, '軍糧丸', 200, 'MilitaryRationsPill_2.png', '外出補給好妙方，增加戰鬥持久力並恢復體力與查克拉。採火之國森林新鮮藥草配製，內含春野櫻獨家配方'),
-- 	(10, '鉗兜羅手裏劍', 1000, 'Shuriken_1.png', '木葉忍者村的強力忍具，每一只皆由25年以上資歷鑄造師精心鑄型，並由10名上忍注入查克拉打造而成!'),
-- 	(11, '剝骨刃', 5000, 'dagger_1.png', '以上忍火燉之術淬鍊成之大馬士革鋼製成，25年資深鑄造師打造，削鐵如泥，取骨如絲滑般柔順，現正特價中!!'),
-- 	(12, '凜月刺刀', 6000, 'bayonet_1.png', '上忍火燉之術淬鍊鈦金，25年以上資歷鑄造師精心鍛造，輕巧鋒利，削鐵如泥，現正特價中!!'),
-- 	(13, '枋田手裏劍', 4000, 'Shuriken_2.png', '特殊的田字造型手裏劍，中央的結構會使發出的手裏劍產生特殊氣旋，加大破壞力與範圍!!'),
-- 	(14, '無相刺刀', 9999, 'bayonet_2.png', '上忍火燉之術淬鍊鈦金，25年以上資歷鑄造師精心鍛造，造型簡約精緻，為七代火影上任時所限量生產的紀念忍具'),
-- 	(15, '蕊拉匕首', 3500, 'dagger_2.png', '上忍火燉之術淬鍊鈦金，25年資深鑄造師打造，有多重機關能展開刀刃，前後端可拆卸，用途多多!!');
/*!40000 ALTER TABLE `myapp_productmodel` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
myapp_productmodel
def main():
	print("############ Testing ship model ############")
	test_ship = hero.Hero();

	print("============ normal horizonatal input test ============")
	test_ship.moveRight(5)
	assert test_ship.getCoordinates() == (0, 5)

	print("============ Zero Horizontal input test ============")
	test_ship.moveRight(0)
	assert test_ship.getCoordinates() == (0, 5)

	print("============ Negative horizontal input test ============")
	test_ship.moveRight(-1)
	assert test_ship.getCoordinates() == (0, 4)

	print("============ normal vertical input test ============")
	test_ship.moveup(5)
	assert test_ship.getCoordinates() == (5, 4)

	print("============ Zero vertical input test ============")
	test_ship.moveRight(0)
	assert test_ship.getCoordinates() == (5, 4)

	print("============ Negative vertical input test ============")
	test_ship.moveRight(-1)
	assert test_ship.getCoordinates() == (4, 4)

	print("============ damage test ============")
	test_ship.getHit()
	assert test_ship.health() == (health - 1)

	print("############ Testing enemy bullet model ############ ")
	enemy_test_bullet = bullet.enemyBullet();

	print("============ enemy bullet movement test ============")
	enemy_test_bullet.update()
	assert enemy_test_bullet.getCoordinates() == (position + speed, y)

	print("############ Testing hero bullet model ############ ")
	hero_test_bullet = bullet.heroBullet();

	print("============ Hero bullet movement test ============")
	hero_test_bullet.update()
	assert Hero_test_bullet.getCoordinates() == (position + speed, y)

	print("============ fire test ============")
	test_ship.fire()
	assert test_bullet == True

	print("############ enemy ship test ############")
	test_enemy = enemy.Enemy()

	print("============ enemy ship movement test ============")
	test_enemy.goLeft(4)
	assert test_enemy.getCoordinates() == (496, 0)

	print("============ enemy destroyed test ============")
	test_enemy.getHit()
	assert test_enemy == False

	Print("############ all tests complete ############")
main()

#pragma strict

function OnTriggerEnter2D (hitInfo : Collider2D) {
	if (hitInfo.name == "Ball")
	{
		var wallName = transform.name;
		ScoreCounter.Score (wallName);
		
		hitInfo.gameObject.SendMessage("resetBall");
	}
}
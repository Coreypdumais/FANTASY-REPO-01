auth_directory = Path(__file__).parent / "auth"
yahoo_query = YahooFantasySportsQuery(
    auth_directory,
    "<league_id>",
    game_id="<game_key>",
    game_code="<game_code>",
    offline=False,
    all_output_as_json=False,
    consumer_key=os.environ["YFPY_CONSUMER_KEY"],
    consumer_secret=os.environ["YFPY_CONSUMER_SECRET"],
    browser_callback=True
)

data_directory = Path(__file__).parent / "output"
data = Data(data_dir)
data.save("file_name", yahoo_query.get_all_yahoo_fantasy_game_keys)
data.load("file_name")

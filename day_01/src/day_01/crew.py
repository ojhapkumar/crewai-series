from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import yaml
from pathlib import Path

load_dotenv()
# Uncomment the following line to use an example of a custom tool
# from day_01.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
# class Day01():
class Day01Crew:
	"""Day01 crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# def __init__(self):
	# 	# Define base directory
	# 	self.base_directory = Path("C:/Workspace/GenAI/pras/crewai-series/day_01/src/day_01")

	# 	# Define agents_config_path as a string or Path
	# 	self.original_agents_config_path = "config/agents.yaml"

	# 	# Resolve the full path
	# 	agents_config_path = self.base_directory / self.original_agents_config_path

	# 	# Load the YAML configuration
	# 	with agents_config_path.open("r") as f:
	# 		self.agents_config = yaml.safe_load(f)

	# # Load the agents_config
	# with open('config/agents.yaml', 'r') as f:
	# 	agents_config = yaml.safe_load(f)

    # # Load the tasks_config
	# with open('config/tasks.yaml', 'r') as f:
	# 	tasks_config = yaml.safe_load(f)

	@agent
	def joke_creator(self) -> Agent:
		# print('in joke_creator',self.agents_config)
		# print()
		# print("Agent config:", self.agents_config['joke_creator'])

		# # Validate agents_config
		# joke_creator_config = self.agents_config.get('joke_creator')
		# if not joke_creator_config:
		# 	raise KeyError("The key 'joke_creator' is missing in agents_config.")

		# # Print for debugging
		# print("Agent config:", joke_creator_config)

		# # Ensure 'key_name' exists in the config
		# if "key_name" not in joke_creator_config:
		# 	raise KeyError("The key 'key_name' is missing in the joke_creator config.")


		return Agent(
			config=self.agents_config['joke_creator'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def add_emojis(self) -> Agent:
		return Agent(
			config=self.agents_config['add_emojis'],
			verbose=True
		)

	@task
	def joke_task(self) -> Task:
		return Task(
			config=self.tasks_config['joke_task'],
		)

	@task
	def add_emojis_task(self) -> Task:
		return Task(
			config=self.tasks_config['add_emojis_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Day01 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

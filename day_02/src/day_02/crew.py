from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Day02():
	"""Day02 crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def chuck_norris_joke_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['chuck_norris_joke_generator'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def chuck_norris_joke_picker(self) -> Agent:
		return Agent(
			config=self.agents_config['chuck_norris_joke_picker'],
			verbose=True
		)

	@task
	def generate_joke_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_joke_task'],
		)

	@task
	def pick_joke_task(self) -> Task:
		return Task(
			config=self.tasks_config['pick_joke_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Day02 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

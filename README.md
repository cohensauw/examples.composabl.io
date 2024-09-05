# Welcome to Your Composabl Trial


For this 14 day trial, you will be able to explore the Composabl platform using a pre-loaded real-world use case.

With your trial, you can:

- View and edit agent components in Python
- Publish Python agent files to the no-code UI
- Create new agent modules using the UI
- Drag and drop modules to create agents
- Train agents and compare their performance

## Who Should Use Composabl

The Composabl platform includes a Python SDK and a no-code UI. This two-part platform reflects that fact that big real-world problems need multiple skill sets at the table: people who work with code, and people who work with processes.

If you are a data scientist or software engineer, you’ll likely spend most of your time using Composabl in the SDK, creating ML and RL models and simulators. So you may want to focus on exploring and editing the Python files in this repository during your trial.

If you’re a process engineer or subject matter expert, on the other hand, you’ll spend most of your time in the no-code UI designing and training agents to succeed in your use cases. This repository is also for you, but you may want to spend less time here and focus on using the UI during your trial.

## Machine Teaching

Composabl is designed to make it easy to implement Machine Teaching, the engineering methodology for creating AI agents. Machine Teaching is a way to infuse human expertise into AI by breaking down tasks into individual skills so that AI can learn more efficiently, perform better, and be more explainable.

This [Machine Teaching tutorial](./Machine-Teaching-Tutorial.md) provides a quick introduction to key concepts applied to the sample use case.

## Use Case Summary

The industrial mixer use case is a realistic case study of an agent controlling a continuous stirred tank chemical reaction. Read more about the case study and the agents that solved it in our whitepaper [Use Cases for Intelligent Agents: Industrial Mixer](https://cdn.prod.website-files.com/65973bba7be64ecd9a0c2ee8/663a811ded2167215bf3b9cf_Industrial%20Mixer%20Whitepaper.pdf).

The industrial mixer agent controls the temperature in a tank where a chemical reaction occurs to create a product.

![chemical tanks](./Sample%20Project:%20Industrial%20Mixer/img/tanks.jpg)

As the chemicals are stirred together in the tank, the reaction produces heat at a nonlinear, unpredictable rate. If the tank isn’t cooled enough, it can reach dangerous temperatures, a condition called thermal runaway. If it’s cooled too much, less product will be produced. The agent needs to balance these two goals, keeping the tank at the right temperature at every moment to maximize production while ensuring safety.

## How to Use This Repository

This GitHub repository contains all the pre-loaded Python files that you can use to create agents. As part of your trial, you can:

- View these files to look under the hood at how they are built
- Edit them to experiment with how changes in the code affects agent design and performance
- Publish them to the UI to use in agents

### Simulator

The simulator is the virtual environment where the agent can practice and learn before trying to control the real system. Explore the [simulator file](./Sample%20Project:%20Industrial%20Mixer/Simulation/20Industrial) to see how Composabl simulators are structured.

<details>

<summary>Learn more about the variables for this use case</summary>
Do you want to know more about the simulator for this use case?
Here are the variables and other information in the simulator your agent will connect to.

##### State Variables
- Ca – Residual (A) concentration – output (y1)
- T (Controlled Variable) – Reactor Temperature (y2)
- Cref – Reference Concentration – Setpoint (SP)
- Tref – Reference Temp- Setpoint (SP)
- Tc (Manipulated Variable) – Coolant Fluid Temperature (u3)
##### Goals
- Minimize Ca (residual concentration)
- Prevent Thermal Runaway
##### Constraints
- dTc +- 10  oC
- T < 400 oC
##### Action (delta MV)
- Tc_adjust – Coolant Fluid Temp Variation
##### Config
- Cref_signal – signal for Cref and Tref
- Noise_percentage – sensor noise
</details>



### Perceptors

[Perceptors](./Sample%20Project:%20Industrial%20Mixer/Perceptors/) are modules that interpret sensor information into new data that the agent can use to make decisions. In this use case, the perceptor is a machine learning model that predicts whether thermal runaway is likely to occur.

### Skills

[Skills](./Sample%20Project:%20Industrial%20Mixer/Skills/) are the parts of an agent that make decisions. The heart of Machine Teaching is decomposing a task into separate skills that can be learned one at a time by deep reinforcement learning or programmed using another control technology. Eight pre-built skills are available in the repository.

### Selectors

[Selectors](./Sample%20Project:%20Industrial%20Mixer/Selectors/) are specialized skills that tell the agent which skill should make a decision based on the conditions reported through the agent’s sensors. Three selectors are available in the repository.

## How to Publish Perceptors, Skills, and Selectors

### Publishing Skills and Selectors

Publishing means uploading a module from the SDK so that it can be used in agents within the SDK.
To publish a skill or selector:
1.	Make sure you have the right version of Python and the right environment.
2.	From the command line, install Composabl: pip install composabl.
3.	The system will redirect you to the UI to enter your credentials and log in.
4.	Return to the command line and navigate to the folder containing the skill or selector you want to publish.
5.	Publish the skill or selector: composabl skill publish or composabl selector publish.
6.	Select your organization from the dropdown menu – in the trial, your only choice will be YOUR_ORGANIZATION_NAME.
7.	Select your project from the dropdown menu. A project is a collection of agents that are all trying to solve the same use case and all use the same simulator. In the trial, you have access to two projects that both use the industrial mixer use case. PRE-BUILT_AGENTS contains agents that are already built and trained for your reference. Your open sandbox is labeled YOUR_ORGANIZATION_NAME_TRIAL. Save your new skill or selector there.
8.	Your skill or selector will begin publishing. When the process is complete, go to the UI, navigate to the Agent Builder Studio, and see your new skill or selector in the sidebar.

### Publishing Perceptors

To publish a perceptor, the process is almost exactly the same except for steps 4 and 5.

4. Navigate to the perceptors folder (one level above the individual perceptor folder).
5. Publish the perceptor: composabl perceptor publish perceptor_name


# Lab 01

# Getting Started

**Objective:** This lab has two purposes:

1. Ensure your development environment is properly set up, whether on lab machines or personal computers.
2. Introduce you to foundational NLP tasks through practical examples.

## Development Environment Options

Depending on your resources and preferences, consider the following setups:

1. **Text Editor and Terminal**

   Using a text editor and a command line terminal to run the python files. This is not recommended, since it is counterproductive (and very frustrating).

2. **Integrated Development Environments (IDEs)**

   Modern IDEs provide comprehensive support for Python development:

   - [**Visual Studio Code**](https://code.visualstudio.com/): A versatile, open-source editor with extensive extensions.
   - [**PyCharm**](https://www.jetbrains.com/pycharm): A robust IDE tailored for Python, offering advanced features.

   These are great tools that are fully integrated and support most needed functions (Including running Jupyter Notebooks). However, the main drawback is that, although you have full control on the setup and installation, they depend on the capability of the machine that are installed. So, if your laptop/desktop is not powerful enough, you will be struggling to run some of the more demanding ML code (e.g. if GPU is needed).

3. **Cloud-Based Platforms**

   Another option, and this is the most recommended, is to host and run the Python code in the Cloud while accessing and interacting with the code remotely via a Web interface. In other words, you will be using your standard browser to access a Web-based IDE that will be running on a machine in the Cloud

   - [**Google Colab**](https://research.google.com/colaboratory): A free platform offering access to GPUs, with seamless integration of Jupyter Notebooks.
   - [**AWS SageMaker Studio Lab**](https://studiolab.sagemaker.aws/): Amazon's offering providing free CPU and GPU resources for machine learning tasks.

   Both platforms are completely free and allows you access to hardware that is capable to run ML code via CPU or GPU. Those IDEs are based on the **Jupyter Notebook** and therefore you can run your code and document your experiments in the same interface. The only notable drawbacks of a Cloud IDE are that, first, that they require an Internet connection, and second, those IDEs are free because the hardware resources are limited by time or capability… although good enough for our purpose of learning.

4. **Local Jupyter Notebook Installation via Anaconda**

   The last option, a very common one actually, is to install the Jupyter Notebooks on your own computer, using [Anaconda](https://www.anaconda.com).

   - **Anaconda Distribution**: A comprehensive package that simplifies the installation of Python and Jupyter Notebooks.

## Setting Up Your Development Environment

1. **Conda Installation**

   If you are going to use your own machine or the labs, make sure Conda is installed and working (should be in the labs)

   - Verify Conda installation:

     ```bash
     conda --version
     ```

   - If Conda is not installed (i.e. might not be on your laptop), then follow the guide to install it: 
       - instructions here (using Anaconda, recommended): [Anaconda installation guide](https://docs.anaconda.com/anaconda/install).
       - or here (bit more advanced, so try Anaconda first): [Advanced installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

2. **Creating a Python Environment**
   
   Note: Creating environments are important in ML / DL to ensure installation consistency for your projects. It also ensures the packages you install do not interfere with future projects. Additionally, it makes sure you have the same installation as everyone else you work with and for preventing some versioning issues. This will also help with your coursework when you work in a group.
   
   You can create environments with the following:

   - Create an environment named `nlp2025` with Python 3.9:

     ```bash
     conda create --name nlp2025 python=3.9
     ```

   - Activate the environment:

     ```bash
     conda activate nlp2025
     ```

   A more detailed guide for managing environments can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

3. **Setting Up in Cloud Platforms**

   For AWS SageMaker Studio Lab users:

   - Access the terminal within the platform.
   - Follow the [AWS setup instructions](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-manage.html) to configure your environment.

## Hardware Considerations for Large Language Models

When working with LLMs, hardware specifications significantly impact performance:

1. **GPU Memory (VRAM)**

    LLMs require substantial VRAM. Models with billions of parameters may need GPUs with **24 GB or more** of VRAM. Running models beyond this threshold is not feasible on consumer-grade laptops, as even the **RTX 5090** is rumored to have only **24 GB** of VRAM.

2. **Optimizing for Low-Powered Devices**

    Recent research have led to **compact LLMs**, which are designed to run efficiently on low-powered hardware. This is primarily achieved through **quantization**, a technique that reduces the precision of a model’s parameters, thereby decreasing its size and computational requirements. You can read more about this [here](https://huggingface.co/docs/optimum/en/concept_guides/quantization), but in essence, you might be able to get some LLMs to run on your local machine if you perform quantization.

3. **Cloud-Based Solutions**

    For those without access to high-end GPUs, **cloud platforms** provide a viable alternative:

    - **Google Colab & AWS SageMaker** offer free and paid access to GPUs.
    - However, note that **session time limits** apply, making them unsuitable for long training processes.
    - Also note that even the highest-tier cloud offerings cannot run **state-of-the-art** models with **400+ billion parameters** (e.g., DeepSeek-R1, Llama 3.1).

4. **Determining Hardware Compatibility**

    To check if your hardware can support a specific LLM, refer to this [GPU Memory Guide](https://ksingh7.medium.com/calculate-how-much-gpu-memory-you-need-to-serve-any-llm-67301a844f21). This resource helps estimate the required GPU memory based on model parameters and precision levels.

    By understanding these limitations and alternatives, you can select the best setup for your LLM projects.



## Your First NLP Lab (2025)

1. **Access the First Lab Repository:**

    The course materials are hosted on GitHub. Access the repository at:  
    **[NLP-2025 GitHub Repository](https://github.com/surrey-nlp/NLP-2025/)**

2. **Clone the Repository:**

    To work with the lab materials, clone the repository into a location accessible by your chosen IDE using the command below:

    ```bash
    git clone https://github.com/surrey-nlp/NLP-2025.git
    ```
    For additional guidance, please refer to the [docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

    This repository will be updated each week with more examples. Alternatively, you can also download the entire code repository as a zip file, but is not recommended for the long term.

3. If you are running the Jupyter Notebook in your local machine or in the labs, make sure you have created and loaded the right Python environment first. If you are
using a Studio Lab, then start a new terminal window and create the environment
there.

4. **Start a Jupyter Notebook:**

    Start a Jupyter Notebook and open *lab02/lab02_Tokenization.ipynb*
    - To run the notebook, see instructions here: https://jupyter.readthedocs.io/en/latest/running.html
    - You could also try JupyterLab for a desktop like IDE like experience (if you are not using the Cloud IDE): https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html

5. Now, just follow the instructions in the notebook.

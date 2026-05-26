<a id="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img width="1530" height="856" alt="image" src="https://github.com/user-attachments/assets/bb3c6920-5f05-4df2-aed4-016d3ce02457" />
  </a>  

  <h1 align="center">Data Anaylsis of Hospitals Across America</h1>

  <p align="center">
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Technologies Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Statistical Methods Used</a>
      <ul>
        <li><a href="#prerequisites">Anova Test</a></li>
        <li><a href="#installation">Paired T-Test</a></li>
        <li><a href="#prerequisites">Two-Sample T-Test</a></li>
        <li><a href="#installation">Chi-Square Test</a></li>
      </ul>
    </li>
    <li><a href="#usage">Key Findings</a></li>
    <li><a href="#roadmap">Dashboard Features</a></li>
    <li><a href="#contributing">Skills Demonstrated</a></li>
    <li><a href="#license">Future Improvements</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<!-- ABOUT THE PROJECT -->

## About The Project


This project explores healthcare cost and hospital rating trends across hospitals in the United States using statistical analysis and data visualization techniques. The analysis focuses on determining whether hospital ratings and procedure costs vary significantly depending on geographic location and procedure type.

Objectives:
* Analyze hospital ratings across states
* Compare healthcare procedure costs
* Identify statistical relationships between state location and hospital performance
* Visualize healthcare trends through interactive dashboards
* Apply real-world statistical methods to healthcare analytics

The dataset contains information from 2,182 hospitals across 53 U.S. states and territories.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Technology Used

Programming & Analysis
* Python
* Pandas
* NumPy
* SciPy
Data Visualization
* PowerBI
* Excel

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Statistical Methods Used

The dataset includes:

|    Variable       |        Type         |         Usage       |
|    --------       |      --------       |        --------     |
| Hospital Ratings  | Ordinal/Categoical  | ANOVA & Chi-Square  |
| Prodcedure Cost   | Nominal/Categorical |  Group Comparisons  |

### 1. ANOVA Test:

* Purpose
  ```sh
  Determine whether hospital ratings significantly differ across states.
  ```
* Hypothesis
  ```sh
  -Null Hypothesis (H₀): Mean hospital ratings are equal across states.
  -Alternative Hypothesis (H₁): At least one state has a different mean hospital rating.
  ```
* Result
  ```sh
  -F-Statistic: 7.8744
  -P-Value: < 0.05
  -Conclusion: Hospital ratings vary significantly by state.
  ```

### 2. Paired T-Test

* Purpose
  ```sh
  Within the same hospital, compare the cost difference between:
      -Heart Attack Procedures
      -Heart Failure Procedures
  ```
* Hypothesis
  ```sh
  -H₀: No significant cost difference exists
  -H₁: Significant cost differences exist
  ```
* Result
  ```sh
  -T-Statistic: 202.9062
  -Conclusion: There is a statistically significant difference between the two procedure costs.
  ```

### 3. Two-Sample T-Test:

* Purpose
  ```sh
  Compare heart attack procedure costs between two states with the largest available datasets.
  ```
* Hypothesis
  ```sh
  -H₀: Mean costs are equal between states
  -H₁: Mean costs differ between states
  ```
* Result
  ```sh
  -T-Statistic: -2.1790
  -P-Value: 0.03
  -Conclusion: Procedure costs significantly differ between states.
  ```

### 4. Chi-Square Test:

* Purpose
  ```sh
  Determine whether there is an association between:
    -State location
    -Hospital rating categories
  ```
* Hypothesis
  ```sh
  -H₀: There is no assoication between hospital location and statewide average rating
  -H₁: There is an assoication between hospital location and statewide average rating
  ```
* Result
  ```sh
  -Chi-Square Statistic: 293.4002
  -Conclusion: There is a significant relationship between hospital ratings and geographic location.
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Key Findings

* Healthcare quality and costs vary significantly depending on location
* States with larger hospital populations tended to have lower overall ratings
* Procedure costs differ substantially across hospitals and states
* Geographic location appears to influence healthcare performance metrics

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Power BI Dashboard Features

**The dashboard includes:**
- [x] Hospital rating breakdowns by state
- [x] Statistical test summaries
- [ ] Chi-Square observed frequency visualizations
- [ ] Overall hospital rating gauge
- [ ] Cost and performance comparisons
  


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Tyler Daniel - [@Tyler.Daniel](www.linkedin.com/in/tyler-daniel-1503841ba) 

<!--Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Read-Me Template]([https://choosealicense.com](https://github.com/othneildrew/Best-README-Template/blob/main/README.md))
* [Pandas Cheat Sheet]([https://www.webpagefx.com/tools/emoji-cheat-sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf))
* [NumPy Documentation]([https://flexbox.malven.co/](https://numpy.org/doc/stable/user/absolute_beginners.html))
* [SciPy Documentation]([https://grid.malven.co/](https://docs.scipy.org/doc/scipy/reference/stats.html))


<p align="right">(<a href="#readme-top">back to top</a>)</p>




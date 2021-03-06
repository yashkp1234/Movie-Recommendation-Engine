# Movie-Recommendation-Engine
My project on analyzing the movie data set,  and creating a recommendation engine using that analysis.

The scripts folder contains all the raw python files used to do the analysis. Please download the Data-set rar file and extract in the same folder as the scripts so that they can be used.

<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Introduction-and-Analysis">Introduction and Analysis<a class="anchor-link" href="#Introduction-and-Analysis">&#182;</a></h1><h2 id="Introduction">Introduction<a class="anchor-link" href="#Introduction">&#182;</a></h2><p>The dataset that I will be using is provided by Kaggle , and is called the “The Movies Dataset”. The dataset contains over 45,000 movies with information about ratings, keywords, directors, cast, and much more. I would like to create a recommendation engine which suggests similar movies based on the movie a user inputs.</p>
<h2 id="Assessing-What-Makes--a-Movie-Good">Assessing What Makes  a Movie Good<a class="anchor-link" href="#Assessing-What-Makes--a-Movie-Good">&#182;</a></h2><p>In order to do this I will first have to define what indicates that a user will like a certain movie, and even simpler than that, what can I use to measure how much a user will like a certain movie. This means before I am able to create this engine I must do some analysis as to what information will be a good factor to consider when recommending the movies.</p>
<h2 id="Filtering-Data">Filtering Data<a class="anchor-link" href="#Filtering-Data">&#182;</a></h2><p>The average rating of a movie will be the metric I will use to measure how “good” a movie is. Any factor which shows evidence of increasing a movies average rating will be considered something important to consider when making the engine.  To remove outliers and data that would make the analysis inaccurate we will filter the database of movies, by only considering movies who have been rated by at least 100 people, and have a runtime between 40 and 180 minutes.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Import Packages</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>   <span class="c1">#importing all the important packages</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">from</span> <span class="nn">ast</span> <span class="k">import</span> <span class="n">literal_eval</span>
<span class="kn">from</span> <span class="nn">operator</span> <span class="k">import</span> <span class="n">itemgetter</span>
<span class="n">pd</span><span class="o">.</span><span class="n">options</span><span class="o">.</span><span class="n">mode</span><span class="o">.</span><span class="n">chained_assignment</span> <span class="o">=</span> <span class="kc">None</span>

<span class="c1">## Define data frames</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;movies_metadata.csv&#39;</span><span class="p">,</span> <span class="n">encoding</span> <span class="o">=</span> <span class="s1">&#39;UTF-8&#39;</span><span class="p">,</span> <span class="n">low_memory</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">df2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;credits.csv&#39;</span><span class="p">,</span> <span class="n">encoding</span> <span class="o">=</span> <span class="s1">&#39;UTF-8&#39;</span><span class="p">,</span> <span class="n">low_memory</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">df3</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;keywords.csv&#39;</span><span class="p">,</span> <span class="n">encoding</span> <span class="o">=</span> <span class="s1">&#39;UTF-8&#39;</span><span class="p">,</span> <span class="n">low_memory</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

<span class="c1">## Filter Movies according to definition</span>
<span class="n">df_fil</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s2">&quot;vote_count&quot;</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">100</span><span class="p">]</span>
<span class="n">df_fil2</span> <span class="o">=</span> <span class="n">df_fil</span><span class="p">[</span><span class="n">df_fil</span><span class="p">[</span><span class="s2">&quot;runtime&quot;</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">40</span><span class="p">]</span>
<span class="n">movie_data</span> <span class="o">=</span> <span class="n">df_fil2</span><span class="p">[</span><span class="n">df_fil2</span><span class="p">[</span><span class="s2">&quot;runtime&quot;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">180</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Lets see what this looks like</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">movie_data</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="n">n</span> <span class="o">=</span> <span class="mi">5</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt output_prompt">Out[2]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>adult</th>
      <th>belongs_to_collection</th>
      <th>budget</th>
      <th>genres</th>
      <th>homepage</th>
      <th>id</th>
      <th>imdb_id</th>
      <th>original_language</th>
      <th>original_title</th>
      <th>overview</th>
      <th>...</th>
      <th>release_date</th>
      <th>revenue</th>
      <th>runtime</th>
      <th>spoken_languages</th>
      <th>status</th>
      <th>tagline</th>
      <th>title</th>
      <th>video</th>
      <th>vote_average</th>
      <th>vote_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>{'id': 10194, 'name': 'Toy Story Collection', ...</td>
      <td>30000000</td>
      <td>[{'id': 16, 'name': 'Animation'}, {'id': 35, '...</td>
      <td>http://toystory.disney.com/toy-story</td>
      <td>862</td>
      <td>tt0114709</td>
      <td>en</td>
      <td>Toy Story</td>
      <td>Led by Woody, Andy's toys live happily in his ...</td>
      <td>...</td>
      <td>1995-10-30</td>
      <td>373554033.0</td>
      <td>81.0</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>
      <td>Released</td>
      <td>NaN</td>
      <td>Toy Story</td>
      <td>False</td>
      <td>7.7</td>
      <td>5415.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>NaN</td>
      <td>65000000</td>
      <td>[{'id': 12, 'name': 'Adventure'}, {'id': 14, '...</td>
      <td>NaN</td>
      <td>8844</td>
      <td>tt0113497</td>
      <td>en</td>
      <td>Jumanji</td>
      <td>When siblings Judy and Peter discover an encha...</td>
      <td>...</td>
      <td>1995-12-15</td>
      <td>262797249.0</td>
      <td>104.0</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}, {'iso...</td>
      <td>Released</td>
      <td>Roll the dice and unleash the excitement!</td>
      <td>Jumanji</td>
      <td>False</td>
      <td>6.9</td>
      <td>2413.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>{'id': 96871, 'name': 'Father of the Bride Col...</td>
      <td>0</td>
      <td>[{'id': 35, 'name': 'Comedy'}]</td>
      <td>NaN</td>
      <td>11862</td>
      <td>tt0113041</td>
      <td>en</td>
      <td>Father of the Bride Part II</td>
      <td>Just when George Banks has recovered from his ...</td>
      <td>...</td>
      <td>1995-02-10</td>
      <td>76578911.0</td>
      <td>106.0</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>
      <td>Released</td>
      <td>Just When His World Is Back To Normal... He's ...</td>
      <td>Father of the Bride Part II</td>
      <td>False</td>
      <td>5.7</td>
      <td>173.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>NaN</td>
      <td>60000000</td>
      <td>[{'id': 28, 'name': 'Action'}, {'id': 80, 'nam...</td>
      <td>NaN</td>
      <td>949</td>
      <td>tt0113277</td>
      <td>en</td>
      <td>Heat</td>
      <td>Obsessive master thief, Neil McCauley leads a ...</td>
      <td>...</td>
      <td>1995-12-15</td>
      <td>187436818.0</td>
      <td>170.0</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}, {'iso...</td>
      <td>Released</td>
      <td>A Los Angeles Crime Saga</td>
      <td>Heat</td>
      <td>False</td>
      <td>7.7</td>
      <td>1886.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>False</td>
      <td>NaN</td>
      <td>58000000</td>
      <td>[{'id': 35, 'name': 'Comedy'}, {'id': 10749, '...</td>
      <td>NaN</td>
      <td>11860</td>
      <td>tt0114319</td>
      <td>en</td>
      <td>Sabrina</td>
      <td>An ugly duckling having undergone a remarkable...</td>
      <td>...</td>
      <td>1995-12-15</td>
      <td>0.0</td>
      <td>127.0</td>
      <td>[{'iso_639_1': 'fr', 'name': 'Français'}, {'is...</td>
      <td>Released</td>
      <td>You are cordially invited to the most surprisi...</td>
      <td>Sabrina</td>
      <td>False</td>
      <td>6.2</td>
      <td>141.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Graphing-and-Analysis">Graphing and Analysis<a class="anchor-link" href="#Graphing-and-Analysis">&#182;</a></h2><p>Now that we have filtered our dataset, we can try to see what information correlates with the average user rating. To visuzlize this we will will use the Seaborn and Matplotlib API. First, we will start with a graph of runtime in relation to rating.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Graph Runtime vs Ratings</span>
<span class="n">g</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">lmplot</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="s2">&quot;runtime&quot;</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="s2">&quot;vote_average&quot;</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="n">movie_data</span><span class="p">,</span>
           <span class="n">size</span> <span class="o">=</span> <span class="mi">6</span><span class="p">,</span> <span class="n">palette</span> <span class="o">=</span> <span class="s2">&quot;YlOrRd&quot;</span><span class="p">,</span> <span class="n">hue</span> <span class="o">=</span> <span class="s2">&quot;runtime&quot;</span><span class="p">,</span> <span class="n">fit_reg</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
           <span class="n">legend</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Runtime in Relation to Ratings&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
gg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>As we can see, there is no clear relationship between the runtime and the average rating. There just a mass of points between 80 - 140 minutes, which makes sense as most movies are around that length, but is not useful for the egnine. The next relationship we will try is the movie popularity and ratings.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">close</span><span class="p">()</span> <span class="c1"># Close previous plot</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">lmplot</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="s2">&quot;popularity&quot;</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="s2">&quot;vote_average&quot;</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="n">movie_data</span><span class="p">,</span>
               <span class="n">size</span> <span class="o">=</span> <span class="mi">6</span><span class="p">,</span> <span class="n">fit_reg</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">legend</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xticklabels</span> <span class="o">=</span> <span class="p">[])</span> <span class="c1"># Remove x labels as they were over crowded</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Popularity in Relation to Ratings&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
RU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Again this graph shows no clear relationship between these two attributes. This leads me to believe that using general movie data is not sufficient. Instead, I will use the credits and the keywords files, so that we can add in more information about each movie such as the directors, cast, and key words that describe the movie. The following will just be function definitions which help retireve the JSON data in the csv files.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">get_actors</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="n">list_acts</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">x</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">i</span><span class="p">[</span><span class="s1">&#39;order&#39;</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">3</span><span class="p">:</span>
            <span class="n">list_acts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">i</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]</span> <span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">list_acts</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="s2">&quot;None&quot;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">list_acts</span>

<span class="k">def</span> <span class="nf">get_director</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">x</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">i</span><span class="p">[</span><span class="s1">&#39;job&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;Director&#39;</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">i</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]</span>
    <span class="k">return</span> <span class="s2">&quot;None&quot;</span>

<span class="k">def</span> <span class="nf">get_keywords</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="n">list_keywords</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">x</span><span class="p">:</span>
        <span class="n">list_keywords</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">list_keywords</span>

<span class="k">def</span> <span class="nf">get_collection</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">x</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">i</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]</span>
    <span class="k">return</span> <span class="s2">&quot;None&quot;</span>

<span class="k">def</span> <span class="nf">get_genres</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="n">list_genres</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">x</span><span class="p">:</span>
        <span class="n">list_genres</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">])</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">list_genres</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span><span class="s2">&quot;None&quot;</span><span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">list_genres</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In the following input, I will declare types from some information in the table so that it can be used for different calculations, and I will merge the tables from the keywords, and credits to the existing movie data table.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;id&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;id&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="s1">&#39;int&#39;</span><span class="p">)</span>
<span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;genres&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;genres&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">literal_eval</span><span class="p">)</span>
<span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;genres&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;genres&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">get_genres</span><span class="p">)</span>
<span class="n">df2</span><span class="p">[</span><span class="s1">&#39;id&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df2</span><span class="p">[</span><span class="s1">&#39;id&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="s1">&#39;int&#39;</span><span class="p">)</span>
<span class="n">df3</span><span class="p">[</span><span class="s1">&#39;id&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df3</span><span class="p">[</span><span class="s1">&#39;id&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="s1">&#39;int&#39;</span><span class="p">)</span>
<span class="n">df2</span><span class="p">[</span><span class="s1">&#39;cast&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df2</span><span class="p">[</span><span class="s1">&#39;cast&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">literal_eval</span><span class="p">)</span>
<span class="n">df2</span><span class="p">[</span><span class="s1">&#39;crew&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df2</span><span class="p">[</span><span class="s1">&#39;crew&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">literal_eval</span><span class="p">)</span>
<span class="n">df2</span><span class="p">[</span><span class="s1">&#39;director&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df2</span><span class="p">[</span><span class="s1">&#39;crew&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">get_director</span><span class="p">)</span>
<span class="n">df2</span><span class="p">[</span><span class="s1">&#39;leads&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df2</span><span class="p">[</span><span class="s1">&#39;cast&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">get_actors</span><span class="p">)</span>
<span class="n">df3</span><span class="p">[</span><span class="s1">&#39;keywords&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df3</span><span class="p">[</span><span class="s1">&#39;keywords&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">literal_eval</span><span class="p">)</span>
<span class="n">df3</span><span class="p">[</span><span class="s1">&#39;keywordz&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df3</span><span class="p">[</span><span class="s1">&#39;keywords&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">get_keywords</span><span class="p">)</span>
<span class="n">movie_data</span> <span class="o">=</span> <span class="n">movie_data</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">df2</span><span class="p">,</span> <span class="n">on</span><span class="o">=</span><span class="s1">&#39;id&#39;</span><span class="p">)</span>
<span class="n">movie_data</span> <span class="o">=</span> <span class="n">movie_data</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">df3</span><span class="p">,</span> <span class="n">on</span><span class="o">=</span><span class="s1">&#39;id&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Lets take a look at our new dataset</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">movie_data</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="n">n</span> <span class="o">=</span> <span class="mi">5</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt output_prompt">Out[7]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>adult</th>
      <th>belongs_to_collection</th>
      <th>budget</th>
      <th>genres</th>
      <th>homepage</th>
      <th>id</th>
      <th>imdb_id</th>
      <th>original_language</th>
      <th>original_title</th>
      <th>overview</th>
      <th>...</th>
      <th>title</th>
      <th>video</th>
      <th>vote_average</th>
      <th>vote_count</th>
      <th>cast</th>
      <th>crew</th>
      <th>director</th>
      <th>leads</th>
      <th>keywords</th>
      <th>keywordz</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>{'id': 10194, 'name': 'Toy Story Collection', ...</td>
      <td>30000000</td>
      <td>[Animation, Comedy, Family]</td>
      <td>http://toystory.disney.com/toy-story</td>
      <td>862</td>
      <td>tt0114709</td>
      <td>en</td>
      <td>Toy Story</td>
      <td>Led by Woody, Andy's toys live happily in his ...</td>
      <td>...</td>
      <td>Toy Story</td>
      <td>False</td>
      <td>7.7</td>
      <td>5415.0</td>
      <td>[{'cast_id': 14, 'character': 'Woody (voice)',...</td>
      <td>[{'credit_id': '52fe4284c3a36847f8024f49', 'de...</td>
      <td>John Lasseter</td>
      <td>[Tom Hanks, Tim Allen, Don Rickles]</td>
      <td>[{'id': 931, 'name': 'jealousy'}, {'id': 4290,...</td>
      <td>[jealousy, toy, boy, friendship, friends, riva...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>NaN</td>
      <td>65000000</td>
      <td>[Adventure, Fantasy, Family]</td>
      <td>NaN</td>
      <td>8844</td>
      <td>tt0113497</td>
      <td>en</td>
      <td>Jumanji</td>
      <td>When siblings Judy and Peter discover an encha...</td>
      <td>...</td>
      <td>Jumanji</td>
      <td>False</td>
      <td>6.9</td>
      <td>2413.0</td>
      <td>[{'cast_id': 1, 'character': 'Alan Parrish', '...</td>
      <td>[{'credit_id': '52fe44bfc3a36847f80a7cd1', 'de...</td>
      <td>Joe Johnston</td>
      <td>[Robin Williams, Jonathan Hyde, Kirsten Dunst]</td>
      <td>[{'id': 10090, 'name': 'board game'}, {'id': 1...</td>
      <td>[board game, disappearance, based on children'...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>{'id': 96871, 'name': 'Father of the Bride Col...</td>
      <td>0</td>
      <td>[Comedy]</td>
      <td>NaN</td>
      <td>11862</td>
      <td>tt0113041</td>
      <td>en</td>
      <td>Father of the Bride Part II</td>
      <td>Just when George Banks has recovered from his ...</td>
      <td>...</td>
      <td>Father of the Bride Part II</td>
      <td>False</td>
      <td>5.7</td>
      <td>173.0</td>
      <td>[{'cast_id': 1, 'character': 'George Banks', '...</td>
      <td>[{'credit_id': '52fe44959251416c75039ed7', 'de...</td>
      <td>Charles Shyer</td>
      <td>[Steve Martin, Diane Keaton, Martin Short]</td>
      <td>[{'id': 1009, 'name': 'baby'}, {'id': 1599, 'n...</td>
      <td>[baby, midlife crisis, confidence, aging, daug...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>NaN</td>
      <td>60000000</td>
      <td>[Action, Crime, Drama, Thriller]</td>
      <td>NaN</td>
      <td>949</td>
      <td>tt0113277</td>
      <td>en</td>
      <td>Heat</td>
      <td>Obsessive master thief, Neil McCauley leads a ...</td>
      <td>...</td>
      <td>Heat</td>
      <td>False</td>
      <td>7.7</td>
      <td>1886.0</td>
      <td>[{'cast_id': 25, 'character': 'Lt. Vincent Han...</td>
      <td>[{'credit_id': '52fe4292c3a36847f802916d', 'de...</td>
      <td>Michael Mann</td>
      <td>[Al Pacino, Robert De Niro, Val Kilmer]</td>
      <td>[{'id': 642, 'name': 'robbery'}, {'id': 703, '...</td>
      <td>[robbery, detective, bank, obsession, chase, s...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>NaN</td>
      <td>58000000</td>
      <td>[Comedy, Romance]</td>
      <td>NaN</td>
      <td>11860</td>
      <td>tt0114319</td>
      <td>en</td>
      <td>Sabrina</td>
      <td>An ugly duckling having undergone a remarkable...</td>
      <td>...</td>
      <td>Sabrina</td>
      <td>False</td>
      <td>6.2</td>
      <td>141.0</td>
      <td>[{'cast_id': 1, 'character': 'Linus Larrabee',...</td>
      <td>[{'credit_id': '52fe44959251416c75039da9', 'de...</td>
      <td>Sydney Pollack</td>
      <td>[Harrison Ford, Julia Ormond, Greg Kinnear]</td>
      <td>[{'id': 90, 'name': 'paris'}, {'id': 380, 'nam...</td>
      <td>[paris, brother brother relationship, chauffeu...</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now using this data frame I will create lists to be used to store specific data about each column. I will also create functions which will define the average rating for each director and each actor.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[66]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">titles</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;title&#39;</span><span class="p">])</span>
<span class="n">keywords</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;keywordz&#39;</span><span class="p">])</span>
<span class="n">directors</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;director&#39;</span><span class="p">])</span>
<span class="n">leads</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;leads&#39;</span><span class="p">])</span>
<span class="n">genres</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;genres&#39;</span><span class="p">])</span>
<span class="n">collections</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;belongs_to_collection&#39;</span><span class="p">])</span>
<span class="n">year</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;release_date&#39;</span><span class="p">])</span>
<span class="n">adult</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;adult&#39;</span><span class="p">])</span>
<span class="n">ratings</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;vote_average&#39;</span><span class="p">])</span>
<span class="n">language</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">movie_data</span><span class="p">[</span><span class="s1">&#39;original_language&#39;</span><span class="p">])</span>
<span class="n">directors2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">directors</span><span class="p">)</span>
<span class="n">titles2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">titles</span><span class="p">)</span>

<span class="c1">## Rounds a number to two decimal points</span>
<span class="k">def</span> <span class="nf">round_two</span> <span class="p">(</span><span class="n">floating</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">float</span><span class="p">(</span><span class="nb">format</span><span class="p">(</span><span class="n">floating</span><span class="p">,</span> <span class="s2">&quot;.2f&quot;</span><span class="p">))</span>

<span class="c1">## Remove duplicates</span>
<span class="k">def</span> <span class="nf">remove_dups</span> <span class="p">(</span><span class="n">list_ex</span><span class="p">):</span>
    <span class="n">already_seen</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">list_ex</span><span class="p">)):</span>
        <span class="k">if</span> <span class="n">list_ex</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">!=</span> <span class="s2">&quot;None&quot;</span> <span class="ow">and</span> <span class="n">list_ex</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">already_seen</span><span class="p">:</span>
            <span class="n">already_seen</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">list_ex</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">already_seen</span>

<span class="c1">## Given an input of a directors name, output the directors average rating</span>
<span class="k">def</span> <span class="nf">get_dir_ave</span> <span class="p">(</span><span class="n">dir_name</span><span class="p">):</span>
    <span class="n">indices</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">directors2</span> <span class="o">==</span> <span class="n">dir_name</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">total</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">indices</span><span class="p">)):</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">indices</span><span class="p">[</span><span class="n">x</span><span class="p">]</span>
        <span class="n">total</span> <span class="o">=</span> <span class="n">total</span> <span class="o">+</span> <span class="n">ratings</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
    <span class="k">return</span> <span class="p">(</span><span class="n">total</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">indices</span><span class="p">))</span>

<span class="c1">## Create genres list</span>
<span class="k">def</span> <span class="nf">create_genre_list</span> <span class="p">():</span>
    <span class="n">gen_ave</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">count</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">genre_fil</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">genres</span><span class="p">)):</span>
        <span class="k">if</span> <span class="n">genres</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s2">&quot;None&quot;</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">genres</span><span class="p">[</span><span class="n">x</span><span class="p">])):</span>
                <span class="n">genre</span> <span class="o">=</span> <span class="n">genres</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span>
                <span class="k">if</span> <span class="n">genre</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">genre_fil</span><span class="p">:</span>
                    <span class="n">genre_fil</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">genre</span><span class="p">)</span>
                    <span class="n">count</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
                    <span class="n">gen_ave</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">ratings</span><span class="p">[</span><span class="n">x</span><span class="p">]))</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">index</span> <span class="o">=</span> <span class="n">genre_fil</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">genre</span><span class="p">)</span>
                    <span class="n">count_ind</span> <span class="o">=</span> <span class="n">count</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
                    <span class="n">count_ind</span> <span class="o">+=</span> <span class="mi">1</span>
                    <span class="n">count</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">count_ind</span>
                    <span class="n">gen_ave</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">gen_ave</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">+</span> <span class="n">ratings</span><span class="p">[</span><span class="n">y</span><span class="p">]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">gen_ave</span><span class="p">)):</span>                
        <span class="n">gen_ave</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">=</span> <span class="n">round_two</span><span class="p">(</span><span class="n">gen_ave</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">/</span> <span class="n">count</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>                                       
    <span class="k">return</span> <span class="p">[</span><span class="n">gen_ave</span><span class="p">,</span> <span class="n">genre_fil</span><span class="p">,</span> <span class="n">count</span><span class="p">]</span>

<span class="c1"># Creates list of all actor names and list which contains their ratings</span>
<span class="k">def</span> <span class="nf">create_act_list</span> <span class="p">():</span>
    <span class="n">act_ave</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">count</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">acts</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">leads</span><span class="p">)):</span>
        <span class="k">if</span> <span class="n">leads</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s2">&quot;None&quot;</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">leads</span><span class="p">[</span><span class="n">x</span><span class="p">])):</span>
                <span class="n">act</span> <span class="o">=</span> <span class="n">leads</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span>
                <span class="k">if</span> <span class="n">act</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">acts</span><span class="p">:</span>
                    <span class="n">acts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">act</span><span class="p">)</span>
                    <span class="n">count</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
                    <span class="n">act_ave</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">ratings</span><span class="p">[</span><span class="n">x</span><span class="p">]))</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">index</span> <span class="o">=</span> <span class="n">acts</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">act</span><span class="p">)</span>
                    <span class="n">count</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
                    <span class="n">act_ave</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">act_ave</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">+</span> <span class="n">ratings</span><span class="p">[</span><span class="n">x</span><span class="p">]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">act_ave</span><span class="p">)):</span>                
        <span class="n">act_ave</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">=</span> <span class="n">round_two</span><span class="p">(</span><span class="n">act_ave</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">/</span> <span class="n">count</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>                                       
    <span class="k">return</span> <span class="p">[</span><span class="n">act_ave</span><span class="p">,</span> <span class="n">acts</span><span class="p">]</span>

<span class="c1">##  Create list of average director ratings</span>
<span class="k">def</span> <span class="nf">create_dir_ave</span> <span class="p">():</span>
    <span class="n">dir_ave</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">dir_fil</span><span class="p">)):</span>
        <span class="n">average</span> <span class="o">=</span> <span class="n">get_dir_ave</span><span class="p">(</span><span class="n">dir_fil</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>
        <span class="n">dir_ave</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">round_two</span><span class="p">(</span><span class="n">average</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">dir_ave</span>

<span class="c1">## Define some lists to be used later on in data visualization</span>
<span class="n">dir_fil</span> <span class="o">=</span> <span class="n">remove_dups</span><span class="p">(</span><span class="n">directors2</span><span class="p">)</span>
<span class="n">list_actors_and_ave</span> <span class="o">=</span> <span class="n">create_act_list</span><span class="p">()</span>
<span class="n">actor_average</span> <span class="o">=</span> <span class="n">list_actors_and_ave</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">actors</span> <span class="o">=</span> <span class="n">list_actors_and_ave</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="n">gen_and_ave</span> <span class="o">=</span> <span class="n">create_genre_list</span><span class="p">()</span>
<span class="n">gen_count</span> <span class="o">=</span> <span class="n">gen_and_ave</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
<span class="n">genres_filtered</span> <span class="o">=</span> <span class="n">gen_and_ave</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="n">gen_averages</span> <span class="o">=</span> <span class="n">gen_and_ave</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">dir_ave_rate</span> <span class="o">=</span> <span class="n">create_dir_ave</span><span class="p">()</span>
<span class="n">mean_actor</span> <span class="o">=</span> <span class="n">round_two</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">actor_average</span><span class="p">)</span><span class="o">.</span><span class="n">mean</span><span class="p">())</span>
<span class="n">mean_genre</span> <span class="o">=</span> <span class="n">round_two</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">gen_averages</span><span class="p">)</span><span class="o">.</span><span class="n">mean</span><span class="p">())</span>
<span class="n">mean_director</span> <span class="o">=</span> <span class="n">round_two</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">dir_ave_rate</span><span class="p">)</span><span class="o">.</span><span class="n">mean</span><span class="p">())</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now we will look at a sample of directors and see where each individual director's average movie rating is in relation to the mean director rating. I will be using a small sample for the directors as, displaying all of the directors in one graph will be very difficult.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_dir</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">sample_ave</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">dir_fil</span><span class="p">)):</span>
    <span class="k">if</span> <span class="n">x</span> <span class="o">%</span> <span class="mi">84</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">sample_dir</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dir_fil</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>
        <span class="n">sample_ave</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dir_ave_rate</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>

<span class="n">sample_dir</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;Mean Rating&quot;</span><span class="p">)</span>
<span class="n">sample_ave</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">mean_director</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="n">sample_dir</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">sample_ave</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">set_xticklabels</span><span class="p">(</span><span class="n">sample_dir</span><span class="p">,</span> <span class="n">rotation</span><span class="o">=</span><span class="mi">90</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Directors Average Film Rating&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">30</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">&quot;Average Film Rating&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s2">&quot;Director&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAdIAAAGHCAYAAAAEI9NyAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo
dHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzsnXe4HVXVh98fJEDoLXRC6Bakhq5I
k6p0BBRFFAMqTawIfAg2UERpltB7N/QWunQSCF0QCV1MEIEQOqzvj7UPd+7cmXPm5Nx7z+He9T7P
POfMzJo9a2b2zNpl7bVlZgRBEARBMH3M0G4FgiAIguDjTBjSIAiCIGiBMKRBEARB0AJhSIMgCIKg
BcKQBkEQBEELhCENgiAIghboCEMqydJyc7t1CYLg44ukL2a+Jz8skRmf9r/R3/oFXUg6KvOsRrVb
n1YYUlVQUtmA03eB14HXgGeA+4C7gSvN7K2WNfyYI2luYP+0OtHMLmmnPp2KpBuADdPqG8DCZhYf
ukGEpD2AE5s87DNm9nBf6NOJSNobOK5k9/v4t/hp4B7gTDO7o59UQ9IawBZp9QIze7S/zt1uKhvS
OswEzJ+Wpen6GL4q6XTgUDN7rRfO83FlbuDQ9P90IAxpDklLABtkNs0O7Aic2h6NguBjyRBg3rSs
Cuwl6TxgdzN7ux/OvwZd37qHgTCkDdg281/AXMA8wMrAesBI3IDsB2wvaRczu60sMTPTdOoRDAy+
geejLLsThnQwcz1wQgW5Z7IrZnYFPfPSQOUqutfghwALA5sCW6ZtO+M11a/1r2qNMbMfAoXN7x83
psuQ1muelCRgc+CPwLLAYsCVktYxs0emS8tgwJLyy25pdQreJLUl8DlJy5jZk21TLmgnz0Q3SEMm
ldyj4yR9BTg7re8q6fdmNrEfdRtU9LqzkTlXAaOAWi10TuBCSR3h3BR0FOsDS6b/5wGnZPZ9o7+V
CYKBgJmdA1yT2fSldukyGOgzw2ZmrwNfBl5Nmz4J7FQk28hrV9JpGZmRadt2ki6T9Kykd8ucoSTN
JOlbSfY5SW9LelXSg5J+X0uvCpKWk/RbSfdKmiLpPUmvSbpP0gmSNko1LCSNTDpNyiSxW+Y6skuh
DpLWlDRG0uOSpkqaJulfkk6XtGHRMbnju91XSfNIOjDp/3Lad1rumLkl/UTSLZImp3v7uqSnJN0h
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
TkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>From this graph we can see that specific directions have significantly lower ratings than others. This provides some indication that the director of a movie effects the movie's rating. Continuing on from this let’s see if directors with more movies under their belt have a higher ratings than those who do not.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_dir2</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">sample_ave2</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">dir_fil</span><span class="p">)):</span>
    <span class="n">indices</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">directors2</span> <span class="o">==</span> <span class="n">dir_fil</span><span class="p">[</span><span class="n">x</span><span class="p">])[</span><span class="mi">0</span><span class="p">]</span>
    <span class="k">if</span> <span class="n">x</span> <span class="o">%</span> <span class="mi">10</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">indices</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">5</span><span class="p">:</span>
        <span class="n">sample_dir2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dir_fil</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>
        <span class="n">sample_ave2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dir_ave_rate</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>

<span class="n">sample_dir2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;Mean Rating&quot;</span><span class="p">)</span>
<span class="n">sample_ave2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">mean_director</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
<span class="n">h</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="n">sample_dir2</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">sample_ave2</span><span class="p">)</span>
<span class="n">h</span><span class="o">.</span><span class="n">set_xticklabels</span><span class="p">(</span><span class="n">sample_dir2</span><span class="p">,</span> <span class="n">rotation</span><span class="o">=</span><span class="mi">90</span><span class="p">)</span>
<span class="n">h</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Directors Average Film Rating&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">30</span><span class="p">)</span>
<span class="n">h</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">&quot;Average Film Rating&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
<span class="n">h</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s2">&quot;Director&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now we can see that directors who have made more films are more likely to have a higher average rating. This could have multiple meanings, one could be that specific directors produce movies in a way that people enjoy and thus they have higher ratings or maybe the more films a director creates the better they get. Regardless, not only does the director effect a films rating but, specifically the more movies a director has made the more of an effect it will have. Now we will move on to the actors.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[65]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_act</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">sample_ave3</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">actors</span><span class="p">)):</span>
    <span class="k">if</span> <span class="n">x</span> <span class="o">%</span> <span class="mi">253</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">sample_act</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">actors</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>
        <span class="n">sample_ave3</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">actor_average</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>

<span class="n">sample_act</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;Mean Rating&quot;</span><span class="p">)</span>
<span class="n">sample_ave3</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">mean_actor</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">clf</span><span class="p">()</span>
<span class="n">i</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="n">sample_act</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">sample_ave3</span><span class="p">)</span>
<span class="n">i</span><span class="o">.</span><span class="n">set_xticklabels</span><span class="p">(</span><span class="n">sample_act</span><span class="p">,</span> <span class="n">rotation</span><span class="o">=</span><span class="mi">90</span><span class="p">)</span>
<span class="n">i</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Actors Average Film Rating&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">30</span><span class="p">)</span>
<span class="n">i</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">&quot;Average Film Rating&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
<span class="n">i</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s2">&quot;Actor&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
IAiCvuT/ABZ/a6cZPBhjAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We can see that the actors follow a similar pattern to the directions, where specific actors significatly above or below the mean rating. This means just like the directors, the actors play a significant role in the movie ratings.</p>
<p>Next we will look at movie genres and how they relate to the average rating using a violin plot. To create this plot I will a select few genres and generate a sample set of ratings for each genre to see how they shape up against each other. Movies do usually have multiply genres, but we will refer to the first genre in the database list as the "main genre".</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[198]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">grab_10_data_points</span><span class="p">(</span><span class="n">genre</span><span class="p">):</span>
    <span class="n">rates</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">genres</span><span class="p">)):</span>
        <span class="k">if</span> <span class="n">x</span> <span class="o">%</span> <span class="mi">15</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">genre</span> <span class="ow">in</span> <span class="n">genres</span><span class="p">[</span><span class="n">x</span><span class="p">]:</span>
                <span class="n">rates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">round_two</span><span class="p">(</span><span class="n">ratings</span><span class="p">[</span><span class="n">x</span><span class="p">]))</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">rates</span><span class="p">)</span> <span class="o">==</span> <span class="mi">10</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">rates</span>

<span class="k">def</span> <span class="nf">re_arrange_data</span><span class="p">(</span><span class="n">pos</span><span class="p">):</span>
    <span class="n">dp_list</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">dp_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">action</span><span class="p">[</span><span class="n">pos</span><span class="p">])</span>
    <span class="n">dp_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">adventure</span><span class="p">[</span><span class="n">pos</span><span class="p">])</span>
    <span class="n">dp_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">comedy</span><span class="p">[</span><span class="n">pos</span><span class="p">])</span>
    <span class="n">dp_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">horror</span><span class="p">[</span><span class="n">pos</span><span class="p">])</span>
    <span class="n">dp_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">family</span><span class="p">[</span><span class="n">pos</span><span class="p">])</span>
    <span class="n">dp_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">mystery</span><span class="p">[</span><span class="n">pos</span><span class="p">])</span>
    <span class="n">dp_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">romance</span><span class="p">[</span><span class="n">pos</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">dp_list</span>

<span class="n">horror</span> <span class="o">=</span> <span class="n">grab_10_data_points</span><span class="p">(</span><span class="s1">&#39;Horror&#39;</span><span class="p">)</span>
<span class="n">comedy</span> <span class="o">=</span> <span class="n">grab_10_data_points</span><span class="p">(</span><span class="s1">&#39;Comedy&#39;</span><span class="p">)</span>
<span class="n">adventure</span> <span class="o">=</span> <span class="n">grab_10_data_points</span><span class="p">(</span><span class="s1">&#39;Adventure&#39;</span><span class="p">)</span>
<span class="n">romance</span> <span class="o">=</span> <span class="n">grab_10_data_points</span><span class="p">(</span><span class="s1">&#39;Romance&#39;</span><span class="p">)</span>
<span class="n">action</span> <span class="o">=</span> <span class="n">grab_10_data_points</span><span class="p">(</span><span class="s1">&#39;Action&#39;</span><span class="p">)</span>
<span class="n">mystery</span> <span class="o">=</span> <span class="n">grab_10_data_points</span><span class="p">(</span><span class="s1">&#39;Mystery&#39;</span><span class="p">)</span>
<span class="n">family</span> <span class="o">=</span> <span class="n">grab_10_data_points</span><span class="p">(</span><span class="s1">&#39;Family&#39;</span><span class="p">)</span>

<span class="n">dp1</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="n">dp2</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dp3</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="n">dp4</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="n">dp5</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span class="n">dp6</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="n">dp7</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">6</span><span class="p">)</span>
<span class="n">dp8</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span>
<span class="n">dp9</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">8</span><span class="p">)</span>
<span class="n">dp10</span> <span class="o">=</span> <span class="n">re_arrange_data</span><span class="p">(</span><span class="mi">9</span><span class="p">)</span>


<span class="n">df_genre</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="p">[</span><span class="n">dp1</span><span class="p">,</span> <span class="n">dp2</span><span class="p">,</span> <span class="n">dp3</span><span class="p">,</span> <span class="n">dp4</span><span class="p">,</span> <span class="n">dp5</span><span class="p">,</span> <span class="n">dp6</span><span class="p">,</span> <span class="n">dp7</span><span class="p">,</span> <span class="n">dp8</span><span class="p">,</span> <span class="n">dp9</span><span class="p">,</span> <span class="n">dp10</span><span class="p">],</span> 
                        <span class="n">columns</span> <span class="o">=</span>  <span class="p">[</span><span class="s2">&quot;Action&quot;</span><span class="p">,</span>  <span class="s2">&quot;Adventure&quot;</span><span class="p">,</span> <span class="s2">&quot;Comedy&quot;</span><span class="p">,</span> <span class="s2">&quot;Horror&quot;</span><span class="p">,</span> <span class="s2">&quot;Family&quot;</span><span class="p">,</span> <span class="s2">&quot;Mystery&quot;</span><span class="p">,</span> <span class="s2">&quot;Romance&quot;</span><span class="p">],</span> 
                        <span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;DP1&quot;</span><span class="p">,</span>  <span class="s2">&quot;DP2&quot;</span><span class="p">,</span> <span class="s2">&quot;DP3&quot;</span><span class="p">,</span> <span class="s2">&quot;DP4&quot;</span><span class="p">,</span> <span class="s2">&quot;DP5&quot;</span><span class="p">,</span> <span class="s2">&quot;DP6&quot;</span><span class="p">,</span> <span class="s2">&quot;DP7&quot;</span><span class="p">,</span> <span class="s2">&quot;DP8&quot;</span><span class="p">,</span> <span class="s2">&quot;DP9&quot;</span><span class="p">,</span> <span class="s2">&quot;DP10&quot;</span><span class="p">])</span>                       
<span class="n">plt</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>            
<span class="n">j</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">violinplot</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">df_genre</span><span class="p">)</span>
<span class="n">j</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Genre Film Ratings&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">25</span><span class="p">)</span>
<span class="n">j</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">&quot;Rating&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
<span class="n">j</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s2">&quot;Genre&quot;</span><span class="p">,</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

                
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This violin plot helps us clearly see that each genre has it own sort of average rating, and a high density of points around that average. This indicates that the genre will be key in recommending movies as since each genre has a diffrent shape, the viewers who watch it have different preferences in terms of what they want in a movie. For example, in this graph the family genre has more movies with ratings in the range of 7 - 9 than any other genre. This shows what kind and quality of a movie the views of that genre will want, and as such we should take into account what genre, and specifically the main genre of a movie to recommend other similar ones.</p>
<p>Now I believe this information we have gathered from our analysis, and some extra information in the database such as category, keywords, and year released will be enough to make our recommendation engine.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Recommendation-Engine">Recommendation Engine<a class="anchor-link" href="#Recommendation-Engine">&#182;</a></h1><h2 id="Description">Description<a class="anchor-link" href="#Description">&#182;</a></h2><p>This recommendation engine will consider the following things directors, keywords, actors, genres, collections, years, ratings, adult, language and index for each movie and score all other movies based on these categories. I believe the director should be weighted slightly heavier than the actors as there are more possibilities for movies to have similar lead actors, but there is only one director. The genres and keywords should also be weighted roughly the same amount to ensure movies that are recommended are similar to the one inputted. The collections or the series it belongs to will be considered so that if a movie of a certain series is inputted then only movies that a sequels are recommended and not prequels. The language and adult are used to ensure movies of the same language or of erotic nature are recommended if the movie inputted is of that nature.</p>
<h2 id="Function-Definitions">Function Definitions<a class="anchor-link" href="#Function-Definitions">&#182;</a></h2><p>To begin we must create a function which which can retrieve this data based on a movie index and store it in a list so that it can be easily accessed.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[173]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Fuction retrieves data of movie based on index inputted</span>
<span class="k">def</span> <span class="nf">retrieve_data</span> <span class="p">(</span><span class="n">index</span><span class="p">):</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">titles</span><span class="p">[</span><span class="n">index</span><span class="p">],</span> <span class="n">directors</span><span class="p">[</span><span class="n">index</span><span class="p">],</span> <span class="n">keywords</span><span class="p">[</span><span class="n">index</span><span class="p">],</span>
            <span class="n">leads</span><span class="p">[</span><span class="n">index</span><span class="p">],</span> <span class="n">genres</span><span class="p">[</span><span class="n">index</span><span class="p">],</span> <span class="n">collections</span><span class="p">[</span><span class="n">index</span><span class="p">],</span>
            <span class="n">year</span><span class="p">[</span><span class="n">index</span><span class="p">],</span> <span class="n">adult</span><span class="p">[</span><span class="n">index</span><span class="p">],</span> <span class="n">ratings</span><span class="p">[</span><span class="n">index</span><span class="p">],</span> <span class="n">index</span><span class="p">,</span> <span class="n">language</span><span class="p">[</span><span class="n">index</span><span class="p">]]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Next we must create a function which can score a movie based on the data retrieved from the previous function.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[174]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Scores each movie based on the inputted movie known as data_list1, and the movie being score data_list2</span>
<span class="k">def</span> <span class="nf">scorer</span><span class="p">(</span><span class="n">data_list1</span><span class="p">,</span> <span class="n">data_list2</span><span class="p">):</span>
    <span class="n">score</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">year1</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">data_list1</span><span class="p">[</span><span class="mi">6</span><span class="p">])[</span><span class="mi">0</span><span class="p">:</span><span class="mi">4</span><span class="p">])</span>
    <span class="n">year2</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">data_list2</span><span class="p">[</span><span class="mi">6</span><span class="p">])[</span><span class="mi">0</span><span class="p">:</span><span class="mi">4</span><span class="p">])</span>
    <span class="k">if</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span> <span class="c1">## Same director</span>
        <span class="n">indices</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">directors2</span> <span class="o">==</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">1</span><span class="p">])[</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">indices</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">5</span><span class="p">:</span> <span class="c1">## Checks if director has made several movies</span>
            <span class="n">score</span> <span class="o">+=</span> <span class="mi">70</span> <span class="c1">## Higher score if so</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">score</span> <span class="o">+=</span> <span class="mi">40</span> <span class="c1">## Lower if not</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">2</span><span class="p">]:</span> <span class="c1">## Number of keywords that are the same</span>
        <span class="k">if</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">2</span><span class="p">]:</span> 
            <span class="n">score</span> <span class="o">+=</span> <span class="mi">30</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">3</span><span class="p">]:</span> <span class="c1">## Number of actors that are the same</span>
        <span class="k">if</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">3</span><span class="p">]:</span>
            <span class="n">score</span> <span class="o">+=</span> <span class="mi">30</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">4</span><span class="p">]:</span> <span class="c1">## Number of genres that are the same</span>
        <span class="k">if</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">4</span><span class="p">]:</span>
            <span class="n">score</span> <span class="o">+=</span> <span class="mi">20</span>
    <span class="k">if</span> <span class="s2">&quot;Family&quot;</span> <span class="ow">in</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span> <span class="ow">and</span> <span class="s2">&quot;Family&quot;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">4</span><span class="p">]:</span> <span class="c1">## Recommend Family Movies</span>
        <span class="n">score</span> <span class="o">-=</span> <span class="mi">75</span>
    <span class="k">if</span> <span class="s2">&quot;Family&quot;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span> <span class="ow">and</span> <span class="s2">&quot;Family&quot;</span> <span class="ow">in</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">4</span><span class="p">]:</span> <span class="c1">## Removes Family Moviess</span>
        <span class="n">score</span> <span class="o">-=</span> <span class="mi">75</span>
    <span class="k">if</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="mi">0</span><span class="p">]:</span> <span class="c1">## If main genre is the same</span>
        <span class="n">score</span> <span class="o">+=</span> <span class="mi">10</span>
    <span class="k">if</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span> <span class="o">==</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">5</span><span class="p">]:</span> <span class="c1">## Movies belong to the same series</span>
        <span class="k">if</span> <span class="n">year1</span> <span class="o">&gt;</span> <span class="n">year2</span><span class="p">:</span> <span class="c1">## Removes prequels</span>
            <span class="n">score</span> <span class="o">-=</span> <span class="mi">300</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">score</span> <span class="o">+=</span> <span class="mi">50000</span> <span class="o">/</span> <span class="p">(</span> <span class="p">(</span><span class="n">year2</span> <span class="o">-</span> <span class="n">year1</span><span class="p">)</span> <span class="o">*</span> <span class="mi">7</span><span class="p">)</span> <span class="c1">## Sequels recommended in order</span>
    <span class="k">if</span>  <span class="n">data_list1</span><span class="p">[</span><span class="mi">7</span><span class="p">]</span> <span class="o">==</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">7</span><span class="p">]:</span> <span class="c1">## Adult nature check</span>
        <span class="n">score</span> <span class="o">+=</span> <span class="mi">100</span>
    <span class="n">score</span> <span class="o">+=</span> <span class="nb">int</span><span class="p">(</span><span class="n">data_list2</span><span class="p">[</span><span class="mi">8</span><span class="p">])</span> <span class="o">*</span> <span class="mi">3</span> <span class="c1">## Scores movies of higher rating higher</span>
    <span class="k">if</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">9</span><span class="p">]</span> <span class="o">==</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">9</span><span class="p">]:</span> <span class="c1">## Remove duplicate movies</span>
        <span class="n">score</span> <span class="o">-=</span> <span class="mi">500</span>
    <span class="k">if</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">10</span><span class="p">]</span> <span class="o">==</span> <span class="n">data_list2</span><span class="p">[</span><span class="mi">10</span><span class="p">]:</span> <span class="c1">## Scores movies of same language higher</span>
        <span class="n">score</span> <span class="o">+=</span> <span class="mi">100</span>
    <span class="k">return</span> <span class="n">score</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Finally we must create the recommendations function and the engine function.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[175]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">create_reccomendations</span><span class="p">(</span><span class="n">data_list1</span><span class="p">):</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">titles</span><span class="p">)):</span>
        <span class="k">if</span> <span class="n">data_list1</span><span class="p">[</span><span class="mi">9</span><span class="p">]</span> <span class="o">==</span> <span class="n">x</span><span class="p">:</span>
            <span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">x</span><span class="p">,</span> <span class="o">-</span><span class="mi">1000</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">x</span><span class="p">,</span> <span class="n">scorer</span><span class="p">(</span><span class="n">data_list1</span><span class="p">,</span> <span class="n">retrieve_data</span><span class="p">(</span><span class="n">x</span><span class="p">))])</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">scores</span><span class="p">,</span> <span class="n">key</span> <span class="o">=</span> <span class="n">itemgetter</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">reverse</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
    <span class="n">suggestions</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">):</span>
        <span class="n">suggestions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">scores</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">suggestions</span>
        
<span class="k">def</span> <span class="nf">engine</span><span class="p">(</span><span class="n">title</span><span class="p">):</span>
    <span class="n">string</span> <span class="o">=</span> <span class="s2">&quot;Your recommendations are:</span><span class="se">\n\n</span><span class="s2">&quot;</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">titles</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>
        <span class="n">list_data</span> <span class="o">=</span> <span class="n">retrieve_data</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
        <span class="n">scores</span> <span class="o">=</span> <span class="n">create_reccomendations</span><span class="p">(</span><span class="n">list_data</span><span class="p">)</span>
        <span class="n">movie_suggestions</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">scores</span><span class="p">:</span>
            <span class="n">movie_suggestions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">titles</span><span class="p">[</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]])</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">movie_suggestions</span><span class="p">)):</span>
            <span class="n">y</span> <span class="o">=</span> <span class="n">x</span> <span class="o">+</span> <span class="mi">1</span>
            <span class="n">string</span> <span class="o">=</span> <span class="n">string</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">y</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;. &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">movie_suggestions</span><span class="p">[</span><span class="n">x</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span>
        <span class="k">return</span> <span class="n">string</span>
    <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
        <span class="n">string</span> <span class="o">=</span> <span class="s2">&quot;There is no movie of that name located in the database.&quot;</span>
        <span class="k">return</span> <span class="n">string</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now our Movie Recommendation Engine is complete! Let's test it.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[176]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">engine</span><span class="p">(</span><span class="s1">&#39;Cars&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Your recommendations are:

1. Cars 2
2. Cars 3
3. Toy Story 2
4. A Bug&#39;s Life
5. Brother Bear
6. The Pirates! In an Adventure with Scientists!
7. Toy Story
8. Wreck-It Ralph
9. The Lego Movie
10. Kung Fu Panda

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[177]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">engine</span><span class="p">(</span><span class="s1">&#39;The Hunger Games&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Your recommendations are:

1. The Hunger Games: Catching Fire
2. The Hunger Games: Mockingjay - Part 1
3. The Hunger Games: Mockingjay - Part 2
4. Divergent
5. Cirque du Freak: The Vampire&#39;s Assistant
6. Allegiant
7. The 5th Wave
8. Pleasantville
9. The Time Machine
10. Final Fantasy: The Spirits Within

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[178]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">engine</span><span class="p">(</span><span class="s1">&#39;asdsarasdsa&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>There is no movie of that name located in the database.
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[179]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">engine</span><span class="p">(</span><span class="s1">&#39;Deadpool&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Your recommendations are:

1. Captain America: The Winter Soldier
2. Doctor Strange
3. Thor: The Dark World
4. The Avengers
5. Ant-Man
6. Guardians of the Galaxy Vol. 2
7. Captain America: Civil War
8. Iron Man
9. Avengers: Age of Ultron
10. Captain America: The First Avenger

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[180]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">engine</span><span class="p">(</span><span class="s1">&#39;The Wolf of Wall Street&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Your recommendations are:

1. War Dogs
2. The Aviator
3. GoodFellas
4. Gangs of New York
5. The Departed
6. The Big Short
7. Taxi Driver
8. Raging Bull
9. Shutter Island
10. Bringing Out the Dead

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Conclusion">Conclusion<a class="anchor-link" href="#Conclusion">&#182;</a></h1><p>There we have it our engine is running and seems to be outputting a very specialized recommendation list, that is very similar to the movie that is inputted.</p>

</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>

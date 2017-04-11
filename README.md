## Generating representative population for a spatial OS simulation with data drawn from a graph 
This tool produces a population csv file for a SpatialOS simulation based on input data representing the distribution of attributes that should exist in your simulated population. The outputted csv can be used with the Snapshot generator flag `population-file-path = <path to csv file defining population>`. 

See the top-level `README.md` for details. 

## Build process
If you don't have it already, download pip
Run: 
`pip install scipy`
`pip install numpy`
`pip install sklearn`

### How to use

This script generates a population csv based on two key pieces of input: a JSON file defining the key meta-attributes of the population to output, including a list of subgroups the population is split into; and csv files defining the attribute distributions among all groups in the populations.

Run this python script with the tags `inputJSON = <path to json defining population meta-attributes>` and `outputPath = <path to directory where you want the file outputted + / + the name you want to give the csv`. Example command (run from this directory) `python population-path="/Users/me/mypopulationjson.json`

You provide the filepaths to the csv files that define your distributions in the json file.

### Formatting your input json
The input json defines the following meta-attributes of the population to generate. 

`size: An integer giving the size of the population to generate. **Size must be greater than 100** `

`groupsInPopulation: object that maps lists of names of groups in the population, as strings, to the proportion of the population that should be part of that group `

`(Ex. {"ReligionA":.66, "ReligionB":.20, "ReligionC":.14} )`

`attributes: list of attributes that exist in the the population simulation, as strings `

`(Ex. ["Conflict","Aversion to Religion A","Aversion to Religion B", "Aversion to Religion C"])`

`attributeDistributions: an object that maps the names of each group in groupsInPopulation to an object that maps every preference to a csv file with samples representing the distribution of that preference in that group`
    
`Ex: "attributeDistributions": {
      "GroupA":{"Conflict": "/Users/username/Desktop/conflictdistribution.csv","AversiontoGroupA":"/Users/username/Desktop/distributionAversionA1.csv","AversiontoGroupB":"/Users/username/Desktop/distributionAversionB1.csv"},
      "GroupB":{"Conflict": "/Users/username/Desktop/conflictdistribution2.csv","AversiontoGroupA":"/Users/username/Desktop/distributionAversionA2.csv","AversiontoGroupB":"/Users/username/Desktop/distributionAversionB2.csv"}
 }`
 
 `pedestrians: An integer representing the portion of the population to be represented as pedestrians (the rest will be cars)`


Full example of a population_settings.json file:

`{
       "pathToPythonInterpreter":"example/path",
       "size" : "10000",
       "groupsInPopulation": {"GroupA":".66","GroupB":".34"},
       "attributes": ["Conflict","AversiontoGroupA","AversiontoGroupB"],
       "attributeDistributions": {
          "GroupA":{"Conflict": "/Users/jordantaylor/Desktop/PythonPopulatIonGenerator/distribution.csv","AversiontoGroupA":"/Users/jordantaylor/Desktop/PythonPopulatIonGenerator/distribution.csv","AversiontoGroupB":"/Users/jordantaylor/Desktop/PythonPopulatIonGenerator/distribution.csv"},
          "GroupB":{"Conflict": "/Users/jordantaylor/Desktop/PythonPopulatIonGenerator/distribution.csv","AversiontoGroupA":"/Users/jordantaylor/Desktop/PythonPopulatIonGenerator/distribution.csv","AversiontoGroupB":"/Users/jordantaylor/Desktop/PythonPopulatIonGenerator/distribution.csv"}
       },
       "pedestrians": "50"
 }`
 
 For an example of a csv distribution file (probably drawn from a graph) see example_distribution_graph in this folder


### Output file format:
The outputted file should look follow this format.

Example rows from CSV file produced from the population_settings.json file above:

Person Number	Group	  Conflict	        AversiontoGroupA	AversiontoGroupB      prefab
Person0	        GroupA	  0.701830128235	0	                0.708728802941        pedestrian
Person1	        GroupA	  0.843596076989	0	                0.518636633655        car
Person2	        GroupA	  0.0642023129214	0	                0.246913073542        car
Person3	        GroupA	  0.348111377901	0	                0.681500958103        car

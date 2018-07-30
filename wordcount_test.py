
from __future__ import absolute_import

import argparse
import logging
import re
import os
import json



from past.builtins import unicode

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/bella/key.json"


def main(argv=None):
  """Main entry point; defines and runs the wordcount pipeline."""

  PROJECT = 'project-id'
  BUCKET = "cloud storage bucker"

  parser = argparse.ArgumentParser()
  parser.add_argument('--input',
                      dest='input',
                      default='input path',
                      help='Input file to process.')
  parser.add_argument('--output',
                      dest='output',
                      # CHANGE 1/5: The Google Cloud Storage path is required
                      # for outputting the results.
                      default='output path',
                      help='Output file to write results to.')

  known_args, pipeline_args = parser.parse_known_args(argv)
  pipeline_args.extend([
     
      '--runner=DataFlowRunner',
      
      '--PROJECT',
      '--staging_location=gs://somepath/tweets',
      '--temp_location=gs://someptah/TEMP',
      '--job_name=tweet-wordcount-job',
  ])

 # pipeline creation

  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = True
  with beam.Pipeline(options=pipeline_options) as p:


    # Read the text file[pattern] into a PCollection.

    lines = p | ReadFromText(known_args.input)

    # Count the occurrences of each word.
    counts = (
        lines
        | 'Split' >> (beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x))
                      .with_output_types(unicode))
        | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
        | 'GroupAndSum' >> beam.CombinePerKey(sum))
    #counts | 'Print' >> beam.ParDo(lambda (w, c): print('%s: %s' % (word, count)))

    # Format the counts into a PCollection of strings.
    def format_result(word_count):
      (word, count) = word_count
      return '%s: %s' % (word, count)

    output = counts | 'Format' >> beam.Map(format_result)
    #counts | 'Print' >> beam.ParDo(lambda (w, c): print('%s: %s' % (w, c)))
    # Write the output using a "Write" transform that has side effects.
    output | WriteToText(known_args.output)
    #print(output)

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  main()

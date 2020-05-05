```bash
.
├── Bayesian-worker-optimizer
│   ├── BeamOptimizer.py
│   ├── BeamWorker_1.py
│   ├── configs.json
│   ├── results.json
│   └── Summary.ipynb
├── beam_py_env.yml
├── BOHB
│   ├── codecov.yml
│   ├── CONTRIBUTING.md
│   ├── docs
│   │   ├── build
│   │   │   └── html
│   │   │       ├── advanced_examples.html
│   │   │       ├── auto_examples
│   │   │       │   ├── commons.html
│   │   │       │   ├── example_1_local_sequential.html
│   │   │       │   ├── example_2_local_parallel_threads.html
│   │   │       │   ├── example_3_local_parallel_processes.html
│   │   │       │   ├── example_3_warmstarting_visualization.html
│   │   │       │   ├── example_4_cluster.html
│   │   │       │   ├── example_5_keras_worker.html
│   │   │       │   ├── example_5_mnist.html
│   │   │       │   ├── example_5_pytorch_worker.html
│   │   │       │   ├── example_8_mnist_continued.html
│   │   │       │   ├── index.html
│   │   │       │   ├── plot_example_6_analysis.html
│   │   │       │   └── plot_example_7_interactive_plot.html
│   │   │       ├── best_practices.html
│   │   │       ├── contact.html
│   │   │       ├── core
│   │   │       │   ├── config_generator.html
│   │   │       │   ├── dispatcher.html
│   │   │       │   ├── iteration.html
│   │   │       │   ├── master.html
│   │   │       │   ├── nameserver.html
│   │   │       │   ├── result.html
│   │   │       │   ├── visualization.html
│   │   │       │   └── worker.html
│   │   │       ├── core_components.html
│   │   │       ├── _downloads
│   │   │       │   ├── auto_examples_jupyter.zip
│   │   │       │   ├── auto_examples_python.zip
│   │   │       │   ├── commons.ipynb
│   │   │       │   ├── commons.py
│   │   │       │   ├── example_1_local_sequential.ipynb
│   │   │       │   ├── example_1_local_sequential.py
│   │   │       │   ├── example_2_local_parallel_threads.ipynb
│   │   │       │   ├── example_2_local_parallel_threads.py
│   │   │       │   ├── example_3_local_parallel_processes.ipynb
│   │   │       │   ├── example_3_local_parallel_processes.py
│   │   │       │   ├── example_3_warmstarting_visualization.ipynb
│   │   │       │   ├── example_3_warmstarting_visualization.py
│   │   │       │   ├── example_4_cluster.ipynb
│   │   │       │   ├── example_4_cluster.py
│   │   │       │   ├── example_5_keras_worker.ipynb
│   │   │       │   ├── example_5_keras_worker.py
│   │   │       │   ├── example_5_mnist.ipynb
│   │   │       │   ├── example_5_mnist.py
│   │   │       │   ├── example_5_pytorch_worker.ipynb
│   │   │       │   ├── example_5_pytorch_worker.py
│   │   │       │   ├── example_8_mnist_continued.ipynb
│   │   │       │   ├── example_8_mnist_continued.py
│   │   │       │   ├── plot_example_6_analysis.ipynb
│   │   │       │   ├── plot_example_6_analysis.py
│   │   │       │   ├── plot_example_7_interactive_plot.ipynb
│   │   │       │   └── plot_example_7_interactive_plot.py
│   │   │       ├── faq.html
│   │   │       ├── genindex.html
│   │   │       ├── _images
│   │   │       │   ├── sphx_glr_commons_thumb.png
│   │   │       │   ├── sphx_glr_example_1_local_sequential_thumb.png
│   │   │       │   ├── sphx_glr_example_2_local_parallel_threads_thumb.png
│   │   │       │   ├── sphx_glr_example_3_local_parallel_processes_thumb.png
│   │   │       │   ├── sphx_glr_example_4_cluster_thumb.png
│   │   │       │   ├── sphx_glr_example_5_keras_worker_thumb.png
│   │   │       │   ├── sphx_glr_example_5_mnist_thumb.png
│   │   │       │   ├── sphx_glr_example_5_pytorch_worker_thumb.png
│   │   │       │   ├── sphx_glr_example_8_mnist_continued_thumb.png
│   │   │       │   ├── sphx_glr_plot_example_6_analysis_001.png
│   │   │       │   ├── sphx_glr_plot_example_6_analysis_002.png
│   │   │       │   ├── sphx_glr_plot_example_6_analysis_003.png
│   │   │       │   ├── sphx_glr_plot_example_6_analysis_004.png
│   │   │       │   ├── sphx_glr_plot_example_6_analysis_005.png
│   │   │       │   ├── sphx_glr_plot_example_6_analysis_thumb.png
│   │   │       │   ├── sphx_glr_plot_example_7_interactive_plot_001.png
│   │   │       │   ├── sphx_glr_plot_example_7_interactive_plot_002.png
│   │   │       │   └── sphx_glr_plot_example_7_interactive_plot_thumb.png
│   │   │       ├── index.html
│   │   │       ├── license.html
│   │   │       ├── _modules
│   │   │       │   ├── hpbandster
│   │   │       │   │   ├── core
│   │   │       │   │   │   ├── base_config_generator.html
│   │   │       │   │   │   ├── base_iteration.html
│   │   │       │   │   │   ├── dispatcher.html
│   │   │       │   │   │   ├── master.html
│   │   │       │   │   │   ├── nameserver.html
│   │   │       │   │   │   ├── result.html
│   │   │       │   │   │   └── worker.html
│   │   │       │   │   ├── optimizers
│   │   │       │   │   │   ├── bohb.html
│   │   │       │   │   │   ├── hyperband.html
│   │   │       │   │   │   └── randomsearch.html
│   │   │       │   │   └── visualization.html
│   │   │       │   └── index.html
│   │   │       ├── objects.inv
│   │   │       ├── optimizers
│   │   │       │   ├── bohb.html
│   │   │       │   ├── how_to_extend.html
│   │   │       │   ├── hyperband.html
│   │   │       │   └── randomsearch.html
│   │   │       ├── optimizers.html
│   │   │       ├── py-modindex.html
│   │   │       ├── quickstart.html
│   │   │       ├── search.html
│   │   │       ├── searchindex.js
│   │   │       ├── _sources
│   │   │       │   ├── advanced_examples.rst.txt
│   │   │       │   ├── auto_examples
│   │   │       │   │   ├── commons.rst.txt
│   │   │       │   │   ├── example_1_local_sequential.rst.txt
│   │   │       │   │   ├── example_2_local_parallel_threads.rst.txt
│   │   │       │   │   ├── example_3_local_parallel_processes.rst.txt
│   │   │       │   │   ├── example_3_warmstarting_visualization.rst.txt
│   │   │       │   │   ├── example_4_cluster.rst.txt
│   │   │       │   │   ├── example_5_keras_worker.rst.txt
│   │   │       │   │   ├── example_5_mnist.rst.txt
│   │   │       │   │   ├── example_5_pytorch_worker.rst.txt
│   │   │       │   │   ├── example_8_mnist_continued.rst.txt
│   │   │       │   │   ├── index.rst.txt
│   │   │       │   │   ├── plot_example_6_analysis.rst.txt
│   │   │       │   │   └── plot_example_7_interactive_plot.rst.txt
│   │   │       │   ├── best_practices.rst.txt
│   │   │       │   ├── contact.rst.txt
│   │   │       │   ├── core
│   │   │       │   │   ├── config_generator.rst.txt
│   │   │       │   │   ├── dispatcher.rst.txt
│   │   │       │   │   ├── iteration.rst.txt
│   │   │       │   │   ├── master.rst.txt
│   │   │       │   │   ├── nameserver.rst.txt
│   │   │       │   │   ├── result.rst.txt
│   │   │       │   │   ├── visualization.rst.txt
│   │   │       │   │   └── worker.rst.txt
│   │   │       │   ├── core_components.rst.txt
│   │   │       │   ├── faq.rst.txt
│   │   │       │   ├── index.rst.txt
│   │   │       │   ├── license.rst.txt
│   │   │       │   ├── optimizers
│   │   │       │   │   ├── bohb.rst.txt
│   │   │       │   │   ├── how_to_extend.rst.txt
│   │   │       │   │   ├── hyperband.rst.txt
│   │   │       │   │   └── randomsearch.rst.txt
│   │   │       │   ├── optimizers.rst.txt
│   │   │       │   └── quickstart.rst.txt
│   │   │       └── _static
│   │   │           ├── ajax-loader.gif
│   │   │           ├── basic.css
│   │   │           ├── broken_example.png
│   │   │           ├── comment-bright.png
│   │   │           ├── comment-close.png
│   │   │           ├── comment.png
│   │   │           ├── css
│   │   │           │   ├── badge_only.css
│   │   │           │   └── theme.css
│   │   │           ├── doctools.js
│   │   │           ├── documentation_options.js
│   │   │           ├── down.png
│   │   │           ├── down-pressed.png
│   │   │           ├── file.png
│   │   │           ├── fonts
│   │   │           │   ├── fontawesome-webfont.eot
│   │   │           │   ├── fontawesome-webfont.svg
│   │   │           │   ├── fontawesome-webfont.ttf
│   │   │           │   ├── fontawesome-webfont.woff
│   │   │           │   ├── fontawesome-webfont.woff2
│   │   │           │   ├── Lato
│   │   │           │   │   ├── lato-bold.eot
│   │   │           │   │   ├── lato-bolditalic.eot
│   │   │           │   │   ├── lato-bolditalic.ttf
│   │   │           │   │   ├── lato-bolditalic.woff
│   │   │           │   │   ├── lato-bolditalic.woff2
│   │   │           │   │   ├── lato-bold.ttf
│   │   │           │   │   ├── lato-bold.woff
│   │   │           │   │   ├── lato-bold.woff2
│   │   │           │   │   ├── lato-italic.eot
│   │   │           │   │   ├── lato-italic.ttf
│   │   │           │   │   ├── lato-italic.woff
│   │   │           │   │   ├── lato-italic.woff2
│   │   │           │   │   ├── lato-regular.eot
│   │   │           │   │   ├── lato-regular.ttf
│   │   │           │   │   ├── lato-regular.woff
│   │   │           │   │   └── lato-regular.woff2
│   │   │           │   └── RobotoSlab
│   │   │           │       ├── roboto-slab-v7-bold.eot
│   │   │           │       ├── roboto-slab-v7-bold.ttf
│   │   │           │       ├── roboto-slab-v7-bold.woff
│   │   │           │       ├── roboto-slab-v7-bold.woff2
│   │   │           │       ├── roboto-slab-v7-regular.eot
│   │   │           │       ├── roboto-slab-v7-regular.ttf
│   │   │           │       ├── roboto-slab-v7-regular.woff
│   │   │           │       └── roboto-slab-v7-regular.woff2
│   │   │           ├── gallery.css
│   │   │           ├── jquery-3.2.1.js
│   │   │           ├── jquery.js
│   │   │           ├── js
│   │   │           │   ├── modernizr.min.js
│   │   │           │   └── theme.js
│   │   │           ├── minus.png
│   │   │           ├── no_image.png
│   │   │           ├── plus.png
│   │   │           ├── pygments.css
│   │   │           ├── searchtools.js
│   │   │           ├── underscore-1.3.1.js
│   │   │           ├── underscore.js
│   │   │           ├── up.png
│   │   │           ├── up-pressed.png
│   │   │           └── websupport.js
│   │   ├── index.html
│   │   ├── Makefile
│   │   └── source
│   │       ├── advanced_examples.rst
│   │       ├── best_practices.rst
│   │       ├── conf.py
│   │       ├── contact.rst
│   │       ├── core
│   │       │   ├── config_generator.rst
│   │       │   ├── dispatcher.rst
│   │       │   ├── iteration.rst
│   │       │   ├── master.rst
│   │       │   ├── nameserver.rst
│   │       │   ├── result.rst
│   │       │   ├── visualization.rst
│   │       │   └── worker.rst
│   │       ├── core_components.rst
│   │       ├── faq.rst
│   │       ├── index.rst
│   │       ├── license.rst
│   │       ├── optimizers
│   │       │   ├── bohb.rst
│   │       │   ├── how_to_extend.rst
│   │       │   ├── hyperband.rst
│   │       │   └── randomsearch.rst
│   │       ├── optimizers.rst
│   │       ├── quickstart.rst
│   │       └── _templates
│   │           └── layout.html
│   ├── hpbandster
│   │   ├── core
│   │   │   ├── base_config_generator.py
│   │   │   ├── base_iteration.py
│   │   │   ├── configselector.py
│   │   │   ├── configselector.pyc
│   │   │   ├── count.txt
│   │   │   ├── dispatcher.py
│   │   │   ├── __init__.py
│   │   │   ├── __init__.pyc
│   │   │   ├── jobid.txt
│   │   │   ├── master.py
│   │   │   ├── nameserver.py
│   │   │   ├── nameserver.pyc
│   │   │   ├── __pycache__
│   │   │   │   ├── configselector.cpython-37.pyc
│   │   │   │   ├── dispatcher.cpython-37.pyc
│   │   │   │   ├── __init__.cpython-37.pyc
│   │   │   │   ├── master.cpython-37.pyc
│   │   │   │   ├── nameserver.cpython-37.pyc
│   │   │   │   ├── result.cpython-37.pyc
│   │   │   │   └── worker.cpython-37.pyc
│   │   │   ├── result.py
│   │   │   ├── thres_value.py
│   │   │   ├── timer.txt
│   │   │   └── worker.py
│   │   ├── examples
│   │   │   ├── commons.py
│   │   │   ├── example_1_local_sequential.py
│   │   │   ├── example_2_local_parallel_threads.py
│   │   │   ├── example_3_local_parallel_processes.py
│   │   │   ├── example_4_cluster.py
│   │   │   ├── example_5_keras_worker.py
│   │   │   ├── example_5_mnist.py
│   │   │   ├── example_5_pytorch_worker.py
│   │   │   ├── example_5_run
│   │   │   │   ├── configs.json
│   │   │   │   └── results.json
│   │   │   ├── example_8_mnist_continued.py
│   │   │   ├── __init__.py
│   │   │   ├── plot_example_6_analysis.py
│   │   │   ├── plot_example_7_interactive_plot.py
│   │   │   └── README.txt
│   │   ├── __init__.py
│   │   ├── optimizers
│   │   │   ├── bohb.py
│   │   │   ├── config_generators
│   │   │   │   ├── bohb.py
│   │   │   │   ├── h2bo.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── kde.py
│   │   │   │   ├── lcnet.py
│   │   │   │   └── random_sampling.py
│   │   │   ├── h2bo.py
│   │   │   ├── hyperband.py
│   │   │   ├── __init__.py
│   │   │   ├── iterations
│   │   │   │   ├── __init__.py
│   │   │   │   ├── successivehalving.py
│   │   │   │   └── successiveresampling.py
│   │   │   ├── kde
│   │   │   │   ├── __init__.py
│   │   │   │   ├── kernels.py
│   │   │   │   └── mvkde.py
│   │   │   ├── lcnet.py
│   │   │   ├── learning_curve_models
│   │   │   │   ├── arif.py
│   │   │   │   ├── base.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── lcnet.py
│   │   │   ├── __pycache__
│   │   │   │   └── __init__.cpython-37.pyc
│   │   │   └── randomsearch.py
│   │   ├── __pycache__
│   │   │   └── visualization.cpython-37.pyc
│   │   ├── utils.py
│   │   ├── visualization.py
│   │   └── workers
│   │       ├── hpolibbenchmark.py
│   │       └── __init__.py
│   ├── LICENSE
│   ├── README.md
│   ├── setup.py
│   └── tests
│       ├── __init__.py
│       ├── test_config_generators.py
│       ├── test_kde.py
│       ├── test_kernels.py
│       ├── test_result.py
│       ├── test_utils.py
│       └── test_worker.py
├── img
│   ├── beamarchi.drawio
│   ├── beam_archi.png
│   └── TB.PNG
├── post-processing
│   ├── Bistro_plot.py
│   ├── clean_storage.py
│   ├── intercept_finder
│   │   ├── import_data.py
│   │   └── intercept_finder.py
│   ├── json_to_csv.py
│   ├── modechoice_reader.py
│   ├── plot_absErr.py
│   ├── results_json_new.csv
│   └── Urbansim-10k-optimization.png
├── README.md
└── search-space-control
    ├── correlational.py
    ├── initializers.py
    ├── parallelizer.py
    ├── storage
    └── worker.py
```
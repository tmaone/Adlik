# About the benchmark

The benchmark is used to test the adlik serving performance of different models.

## Test the runtime performance

The parameters of the automatic test framework are as follows:

| abbreviation | detail                    | type | help                                          | default                                                             |
| ------------ | ------------------------- | ---- | --------------------------------------------- | ------------------------------------------------------------------- |
| -d           | --docker-file-path        | str  | The docker file path of the test serving type |                                                                     |
| -s           | --serving-type            | str  | The test serving type                         |                                                                     |
| -b           | --build-directory         | str  | The directory which to build the docker       |                                                                     |
| -a           | --adlik-directory         | str  | The adlik directory                           | Adlik                                                               |
| -m           | --model-name              | str  | The path of model used for test               |                                                                     |
| -c           | --client-script           | str  | The script used to infer                      | client_script.sh                                                    |
| -ss          | --serving-script          | str  | The serving script                            | serving_script.sh                                                   |
| -ov          | --openvino-version        | str  | The version of the OpenVINO                   | 2019.3.344                                                          |
| -tt          | --tensorrt-tar            | str  | The tar version of the TensorRT               | TensorRT-7.0.0.11.Ubuntu-18.04.x86_64-gnu.cuda-10.0.cudnn7.6.tar.gz |
| -tv          | --tensorrt-version        | str  | The version of TensorRT                       | 7.0.0.11                                                            |
| -l           | --log-path                | str  | The path of log directory                     | log                                                                 |
| -tm          | --test-model-path         | str  | The path of test model                        |                                                                     |
| -sj          | --serving-json            | str  | The json of model                             | serving_model.json                                                  |
| -cis         | --client-inference-script | str  | The inference script                          |                                                                     |
| -i           | --image-filename          | str  | Input image                                   |                                                                     |
| -gl          | --gpu-label               | int  | The GPU label                                 | None                                                                |
| -cs          | --compile-script          | str  | Compile the model script                      | compile_script.sh                                                   |

If you want to use the automatic_test.py test the runtime, you need to follow the steps below:

1. Download Adlik code.
2. Install docker.
3. Prepare the serving_model.json (required for compile model) trained model, the format of the model file can be: .pb,
.h5, .ckpt, .onnx, savedModel, and it is recommended to put the model and serving_model.json under the
Adlik/benchmark/test/test_model directory.
4. The writing of serving_model.json can refer to the serving_model.json of each model in
Adlki/benchmark/tests/test_model and Adlik/model_compiler/src/model_compiler/config_schema.json.
5. If there is no required inference code in the Adlik/benchmark/test/client directory of the benchmark, you need to
write the inference code
6. Specify the type of test runtime and version number (if needed, eg: OpenVINO and TensorRT).
7. Explicitly test whether a GPU is required.
8. The environment running the code has python3.7 or above installed.
9. According to the runtime type of the test, select the dockerfile, serving script and compile script required by the
test under the Adlik/benchmark/test directory
10. Configure parameters for testing, for example, run the follow command in the Adlik directory:

```sh

python3 benchmark/src/automatic_test.py -d benchmark/test/docker_test/openvino.Dockerfile -s openvino -b . -a . -m mnist
-c benchmark/test/client_script/client_script.sh -ss benchmark/test/serving_script/openvino_serving_script.sh -l
abspath(log) -tm benchmark/test/test_model/mnist_keras -cis mnist_client.py -i mnist.png -cs
benchmark/test/compile_script/compile_script.sh
```

## NOTE

1. If the test tensorrt is running, you need to register and download the dependency package from
[TensorRT](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html). The downloaded dependency
package is recommended to be placed in the Adlik directory.
2. If your local environment has no way to connect to the external network, you need to configure the apt source and pip
source that can be used, and add the configuration command to the Dockerfile.
3. When bazel build, if you can't pull the package, you can also download the required packages in advance, and use the
--distdir command.
4. To prevent the computer from occupying too many cores when bazel build, causing jams. During bazel build, you can
also use --jobs to set concurrent jobs.

from transformers.convert_graph_to_onnx import convert
from pathlib import Path


framework = "pt"
model = "distilbert-base-uncased-finetuned-sst-2-english"
output_dir = "onnx/distilbert.onnx"
opset = 11
task = "text-classification"


def main():
    output = Path(output_dir).absolute()
    print(output)
    convert(framework=framework, model=model, output=output, opset=opset, tokenizer=model, pipeline_name=task)


if __name__ == "__main__":
    main()


# torch.export.onnx(
#     model=task.model,
#     args=(dict(encodings),),
#     f=output_path.as_posix(),
#     input_names=list(config.task.inputs.keys()),
#     output_names=list(config.task.outputs.keys()),
#     opset_version=self.default_opset,
#     dynamic_axes=dict(
#         **{name: dict(v) for name, v in dynamic_inputs_axes.items()},
#         **{name: dict(v) for name, v in dynamic_outputs_axes.items()},
#     ),
#     use_external_data_format=use_external_data_format,
# )

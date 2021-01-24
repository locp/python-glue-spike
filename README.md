# python-glue-spike

A spike to look at developing Python ETL pipelines for Glue locally.  This is
a refinement of a blog (Pathak, 2020) specifically to setting up an
extract, translate & load (ETL) pipeline locally for development and test
purposes.

## Python Version

We use a rather ancient version of Python (3.6.10) in the containers because
that's the version that ships with the AWS provided container.

## Operations

### Cleanup

To shutdown all running containers and clean up any temporary files, run the
following command:

```shell
make clean
```
## References

Pathak, V. (2020). _Developing AWS Glue ETL jobs locally using a container._
[online] AWS Big Data Blog. Available at:
https://aws.amazon.com/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container
[Accessed 23 Jan. 2021].

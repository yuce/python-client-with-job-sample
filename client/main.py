import logging

from hazelcast import HazelcastClient

from hzconfig import load_config


def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config()
    client = HazelcastClient(config)
    print("OK Connected to cluster:", config.cluster_name)
    client.shutdown()


if __name__ == "__main__":
    main()
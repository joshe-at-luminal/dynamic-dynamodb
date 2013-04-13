""" Configuration management """
import config_file_parser
import command_line_parser


DEFAULT_OPTIONS = {
    # Command line only
    'config': None,
    'dry_run': False,

    # [global]
    'aws_region': 'us-east-1',
    'aws_access_key_id': None,
    'aws_secret_access_key': None,
    'check_interval': 300,

    # [logging]
    'log_file': None,
    'log_level': 'info',

    # [table: x]
    'table_name': None,
    'reads_lower_threshold': 30,
    'reads_upper_threshold': 90,
    'increase_reads_with': 50,
    'decrease_reads_with': 50,
    'writes_lower_threshold': 30,
    'writes_upper_threshold': 90,
    'increase_writes_with': 50,
    'decrease_writes_with': 50,
    'min_provisioned_reads': None,
    'max_provisioned_reads': None,
    'min_provisioned_writes': 'apa',
    'max_provisioned_writes': None,
    'allow_scaling_down_reads_on_0_percent': False,
    'allow_scaling_down_writes_on_0_percent': False,
    'always_decrease_rw_together': False,
    'maintenance_windows': None,
}


def get_configuration():
    """ Get the configuration from command line and config files """
    # This is the dict we will return
    configuration = {}

    # Read the command line options
    cmd_line_options = command_line_parser.parse()

    # If a configuration file is specified, read that as well
    if cmd_line_options['config']:
        conf_file_options = config_file_parser.parse(cmd_line_options['config'])

    # Replace any overlapping values so that command line options
    # trumps configuration file options
    for option in DEFAULT_OPTIONS:
        # Get the value from the configuration file
        configuration[option] = conf_file_options.get(
            option, DEFAULT_OPTIONS[option])

        # Get the value from the command line
        configuration[option] = cmd_line_options.get(
            option, DEFAULT_OPTIONS[option])

    return configuration

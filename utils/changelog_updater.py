# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

import requests


def main() -> None:
    """
    Update CHANGELOG.md when API generator produces new code differing from existing.
    """
    response = requests.get(
        "https://api.github.com/repos/opensearch-project/opensearch-api-specification/commits"
    )
    if response.ok:
        commit_info = response.json()[0]
        commit_url = commit_info["html_url"]
        latest_commit_sha = commit_info.get("sha")
    else:
        raise Exception(
            f"Failed to fetch opensearch-api-specification commit information. Status code: {response.status_code}"
        )

    with open("CHANGELOG.md", "r+", encoding="utf-8") as file:
        content = file.read()
        if commit_url not in content:
            if "### Updated APIs" in content:
                file_content = content.replace(
                    "### Updated APIs",
                    f"### Updated APIs\n- Updated opensearch-py APIs to reflect [opensearch-api-specification@{latest_commit_sha[:7]}]({commit_url})",
                    1,
                )
                file.seek(0)
                file.write(file_content)
                file.truncate()
            else:
                raise Exception("'Updated APIs' section is not present in CHANGELOG.md")


if __name__ == "__main__":
    main()
